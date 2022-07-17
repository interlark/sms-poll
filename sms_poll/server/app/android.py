from __future__ import annotations

import threading
from typing import Any, Callable

from .utils import PLATFORM

if PLATFORM == 'android':
    from jnius import autoclass, cast

    from android.broadcast import BroadcastReceiver
    from android.permissions import (Permission, check_permission,
                                     request_permissions)
    ANDROID_VERSION = autoclass('android.os.Build$VERSION')
    SDK_INT = ANDROID_VERSION.SDK_INT


sms_reciever: BroadcastReceiver = None


def ensure_permissions(*permissions: str) -> bool:
    """Ensure we got required permissions,
    request them if needed."""
    if PLATFORM != 'android':
        return True

    ungranted_permissions = [x for x in permissions if not check_permission(x)]
    if not ungranted_permissions:
        return True

    response_result = False
    response_recieved = threading.Event()

    def request_callback(permissions: list[str], grant_results: list[bool]):
        nonlocal response_result
        response_result = all(grant_results)
        response_recieved.set()

    request_permissions(ungranted_permissions, request_callback)

    response_recieved.wait()
    return response_result


def get_android_python_activity() -> Any:
    """Returns the `PythonActivity.mActivity` using `pyjnius`."""
    if PLATFORM != 'android':
        return None

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    return PythonActivity.mActivity


def get_phone_number() -> str:
    """
    Get phone number.

    N.B. Some SIMs do not privide the phone number.
    """
    if PLATFORM != 'android':
        return 'NO PHONE NUMBER'

    if not ensure_permissions(Permission.READ_PHONE_NUMBERS):
        return 'PERMISSIONS NOT GRANTED'

    activity = get_android_python_activity()
    Context = autoclass('android.content.Context')

    if SDK_INT < 33:
        telephony_service = activity.getSystemService(Context.TELEPHONY_SERVICE)
        telephony = cast('android.telephony.TelephonyManager', telephony_service)
        phone_number = telephony.getLine1Number()
    else:
        telephony_subscription_service = activity.getSystemService(
            Context.TELEPHONY_SUBSCRIPTION_SERVICE
        )
        telephony_subscription = cast('android.telephony.SubscriptionManager',
                                      telephony_subscription_service)
        phone_number = telephony_subscription.getPhoneNumber(
            telephony_subscription.DEFAULT_SUBSCRIPTION_ID
        )

    try:
        import phonenumbers
        pn = phonenumbers.parse(phone_number)
        return phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.NATIONAL)
    except (phonenumbers.NumberParseException, ImportError):
        return phone_number.strip()


def get_wifi_ip() -> str:
    """Get Wi-Fi IP address."""
    if PLATFORM != 'android':
        return 'NO WIFI IP FOUND'

    if not ensure_permissions(Permission.ACCESS_WIFI_STATE):
        return 'PERMISSIONS NOT GRANTED'

    activity = get_android_python_activity()
    Context = autoclass('android.content.Context')
    wifi_service = activity.getSystemService(Context.WIFI_SERVICE)
    wifi_manager = cast('android.net.wifi.WifiManager', wifi_service)
    connection_info = wifi_manager.getConnectionInfo()
    ip_int = connection_info.getIpAddress()

    if ip_int == 0:
        return 'NO WIFI IP FOUND'

    ip = '%d.%d.%d.%d' % (ip_int & 0xff, ip_int >> 8 & 0xff,
                          ip_int >> 16 & 0xff, ip_int >> 24 & 0xff)

    return ip


def start_sms_reciever(callback: Callable[[str, str], Any]) -> None:
    """Start listening SMS."""
    def callback_wrapper(callback: Callable[[str, str], Any]) -> Callable[[Any, Any], Any]:
        def inner(context: Any, intent: Any) -> None:
            extras = intent.getExtras()
            if extras:
                SmsMessage = autoclass('android.telephony.SmsMessage')
                for pdu in extras.get('pdus'):
                    sms_message = SmsMessage.createFromPdu(pdu)
                    phone_number = sms_message.getDisplayOriginatingAddress()
                    body = sms_message.getDisplayMessageBody()
                    callback(phone_number, body)

        return inner

    if PLATFORM != 'android':
        return None

    ensure_permissions(Permission.RECEIVE_SMS)

    global sms_reciever
    sms_reciever = BroadcastReceiver(callback_wrapper(callback),
                                     actions=['android.provider.Telephony.SMS_RECEIVED'])
    sms_reciever.start()


def stop_sms_reciever() -> None:
    """Stop listening SMS."""
    if PLATFORM != 'android':
        return None

    global sms_reciever
    if sms_reciever:
        sms_reciever.stop()
        sms_reciever = None
