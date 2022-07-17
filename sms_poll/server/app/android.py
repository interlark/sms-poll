import threading

from .utils import PLATFORM

if PLATFORM == 'android':
    from jnius import autoclass, cast

    from android.broadcast import BroadcastReceiver
    from android.permissions import (Permission, check_permission,
                                     request_permissions)
    ANDROID_VERSION = autoclass('android.os.Build$VERSION')
    SDK_INT = ANDROID_VERSION.SDK_INT


def ensure_permissions(*permissions):
    ungranted_permissions = [x for x in permissions if not check_permission(x)]
    if not ungranted_permissions:
        return True

    response_result = None
    response_recieved = threading.Event()

    def request_callback(permissions, grant_results):
        nonlocal response_result
        response_result = all(grant_results)
        response_recieved.set()

    request_permissions(ungranted_permissions, request_callback)

    response_recieved.wait()
    return response_result

def get_android_python_activity():
    """Returns the `PythonActivity.mActivity` using `pyjnius`."""
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    return PythonActivity.mActivity

def get_phone_number():
    """
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
        telephony_subscription_service = activity.getSystemService(Context.TELEPHONY_SUBSCRIPTION_SERVICE)
        telephony_subscription = cast('android.telephony.SubscriptionManager', telephony_subscription_service)
        phone_number = telephony_subscription.getPhoneNumber(telephony_subscription.DEFAULT_SUBSCRIPTION_ID)

    try:
        import phonenumbers
        pn = phonenumbers.parse(phone_number)
        return phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.NATIONAL)
    except (phonenumbers.NumberParseException, ImportError):
        return phone_number.strip()

def get_wifi_ip():
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


sms_reciever = None
def start_sms_reciever(callback):
    def callback_wrapper(callback):
        def inner(context, intent):
            extras = intent.getExtras()
            if extras:
                SmsMessage = autoclass('android.telephony.SmsMessage')
                for pdu in extras.get('pdus'):
                    sms_message = SmsMessage.createFromPdu(pdu)
                    phone_number = sms_message.getDisplayOriginatingAddress()
                    body = sms_message.getDisplayMessageBody()
                    callback(phone_number, body)

        return inner

    ensure_permissions(Permission.RECEIVE_SMS)

    global sms_reciever
    sms_reciever = BroadcastReceiver(callback_wrapper(callback), actions=['android.provider.Telephony.SMS_RECEIVED'])
    sms_reciever.start()

def stop_sms_reciever():
    global sms_reciever
    if sms_reciever:
        sms_reciever.stop()
        sms_reciever = None
