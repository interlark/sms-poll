import os
import sys


def get_platform():
    # On Android sys.platform returns 'linux2', so prefer to check the
    # existence of environ variables set during Python initialization
    kivy_build = os.environ.get('KIVY_BUILD', '')
    if kivy_build in ('android', 'ios'):
        return kivy_build
    elif 'P4A_BOOTSTRAP' in os.environ:
        return 'android'
    elif 'ANDROID_ARGUMENT' in os.environ:
        # We used to use this method to detect android platform,
        # leaving it here to be backwards compatible with `pydroid3`
        # and similar tools outside kivy's ecosystem
        return 'android'
    elif sys.platform in ('win32', 'cygwin'):
        return 'win'
    elif sys.platform == 'darwin':
        return 'macosx'
    elif sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('freebsd'):
        return 'linux'

    return 'unknown'

PLATFORM = get_platform()
