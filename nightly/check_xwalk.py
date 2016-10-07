#!/usr/bin/env python3

import json
from distutils.version import LooseVersion
import detect_ver
import config

def check_if_has_new_xwalk_for_android_canary():
    '''
    Check if there is new version of Crosswalk binary for Android released.
    Generate a canary.json to store the version information of last update
    and this query, if any update, specify the update key as "True"
    '''
    with open(config.XWALK_ANDROID_VERSION_FILE.get('canary'), 'r') as fp:
        old_ver = fp.read().strip()

    oldVer = LooseVersion(old_ver)

    latest_ver = detect_ver.detect_latest_android('canary')
    print(latest_ver)
    newVer = LooseVersion(latest_ver)

    version_change = {}
    version_change['old_ver'] = old_ver
    version_change['new_ver'] = latest_ver

    if newVer > oldVer:
        with open(config.XWALK_ANDROID_VERSION_FILE.get('canary'), 'w') as fp:
            fp.write(latest_ver)

        version_change['update'] = True
    else:
        version_change['update'] = False

    with open(config.XWALK_ANDROID_UPDATE_JSON_FILE.get('canary'), 'w') as fp:
        json.dump(version_change, fp, indent = 4)


def check_if_has_new_xwalk_for_android_beta21():
    '''
    Check if there is new version of Crosswalk binary for Android released.
    Generate a beta21.json to store the version information of last update
    and this query, if any update, specify the update key as "True"
    '''
    with open(config.XWALK_ANDROID_VERSION_FILE.get('beta21'), 'r') as fp:
        old_ver = fp.read().strip()

    oldVer = LooseVersion(old_ver)

    latest_ver = detect_ver.detect_latest_android('beta')
    print(latest_ver)
    newVer = LooseVersion(latest_ver)

    version_change = {}
    version_change['old_ver'] = old_ver
    version_change['new_ver'] = latest_ver

    if newVer > oldVer:
        with open(config.XWALK_ANDROID_VERSION_FILE.get('beta21'), 'w') as fp:
            fp.write(latest_ver)

        version_change['update'] = True
    else:
        version_change['update'] = False

    with open(config.XWALK_ANDROID_UPDATE_JSON_FILE.get('beta21'), 'w') as fp:
        json.dump(version_change, fp, indent = 4)

		
def check_if_has_new_xwalk_for_android_beta22():
    '''
    Check if there is new version of Crosswalk binary for Android released.
    Generate a beta22.json to store the version information of last update
    and this query, if any update, specify the update key as "True"
    '''
    with open(config.XWALK_ANDROID_VERSION_FILE.get('beta22'), 'r') as fp:
        old_ver = fp.read().strip()

    oldVer = LooseVersion(old_ver)

    latest_ver = detect_ver.detect_latest_android('beta')
    print(latest_ver)
    newVer = LooseVersion(latest_ver)

    version_change = {}
    version_change['old_ver'] = old_ver
    version_change['new_ver'] = latest_ver

    if newVer > oldVer:
        with open(config.XWALK_ANDROID_VERSION_FILE.get('beta22'), 'w') as fp:
            fp.write(latest_ver)

        version_change['update'] = True
    else:
        version_change['update'] = False

    with open(config.XWALK_ANDROID_UPDATE_JSON_FILE.get('beta22'), 'w') as fp:
        json.dump(version_change, fp, indent = 4)		


def check_if_has_new_xwalk_for_windows_canary():
    '''
    Check if there is new version of Crosswalk binary for Windows released.
    Generate a canary.json to store the version information of last update
    and this query, if any update, specify the update key as "True"
    '''
    with open(config.XWALK_WINDOWS_VERSION_FILE.get('canary'), 'r') as fp:
        old_ver = fp.read().strip()

    oldVer = LooseVersion(old_ver)

    latest_ver = detect_ver.detect_latest_windows('canary')
    print(latest_ver)
    newVer = LooseVersion(latest_ver)

    version_change = {}
    version_change['old_ver'] = old_ver
    version_change['new_ver'] = latest_ver

    if newVer > oldVer:
        with open(config.XWALK_WINDOWS_VERSION_FILE.get('canary'), 'w') as fp:
            fp.write(latest_ver)

        version_change['update'] = True
    else:
        version_change['update'] = False

    with open(config.XWALK_WINDOWS_UPDATE_JSON_FILE.get('canary'), 'w') as fp:
        json.dump(version_change, fp, indent = 4)


def check_if_has_new_xwalk_for_windows_beta21():
    '''
    Check if there is new version of Crosswalk binary for Windows released.
    Generate a beta21.json to store the version information of last update
    and this query, if any update, specify the update key as "True"
    '''
    with open(config.XWALK_WINDOWS_VERSION_FILE.get('beta21'), 'r') as fp:
        old_ver = fp.read().strip()

    oldVer = LooseVersion(old_ver)

    latest_ver = detect_ver.detect_latest_windows('beta')
    print(latest_ver)
    newVer = LooseVersion(latest_ver)

    version_change = {}
    version_change['old_ver'] = old_ver
    version_change['new_ver'] = latest_ver

    if newVer > oldVer:
        with open(config.XWALK_WINDOWS_VERSION_FILE.get('beta21'), 'w') as fp:
            fp.write(latest_ver)

        version_change['update'] = True
    else:
        version_change['update'] = False

    with open(config.XWALK_WINDOWS_UPDATE_JSON_FILE.get('beta21'), 'w') as fp:
        json.dump(version_change, fp, indent = 4)


def check_if_has_new_xwalk_for_windows_beta22():
    '''
    Check if there is new version of Crosswalk binary for Windows released.
    Generate a beta22.json to store the version information of last update
    and this query, if any update, specify the update key as "True"
    '''
    with open(config.XWALK_WINDOWS_VERSION_FILE.get('beta22'), 'r') as fp:
        old_ver = fp.read().strip()

    oldVer = LooseVersion(old_ver)

    latest_ver = detect_ver.detect_latest_windows('beta')
    print(latest_ver)
    newVer = LooseVersion(latest_ver)

    version_change = {}
    version_change['old_ver'] = old_ver
    version_change['new_ver'] = latest_ver

    if newVer > oldVer:
        with open(config.XWALK_WINDOWS_VERSION_FILE.get('beta22'), 'w') as fp:
            fp.write(latest_ver)

        version_change['update'] = True
    else:
        version_change['update'] = False

    with open(config.XWALK_WINDOWS_UPDATE_JSON_FILE.get('beta22'), 'w') as fp:
        json.dump(version_change, fp, indent = 4)		