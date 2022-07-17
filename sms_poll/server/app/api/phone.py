from fastapi import APIRouter

from ..android import get_phone_number, get_wifi_ip
from ..config import config

router = APIRouter(prefix='/phone')


if config.debug:
    @router.get('/number')
    def number():
        """Get phone number."""
        return get_phone_number()


@router.get('/wifi_ip')
def wifi_ip():
    """Get phone Wi-Fi IP address."""
    return get_wifi_ip()
