#!/usr/bin/env python3


import os
import sys
import urllib.parse

import requests

import config


def download_file(url, filename, use_wget = False):
    if not use_wget:
        print('downloading {url}'.format(url = url))
        conn = requests.get(url, verify = False)
        if conn.status_code == 200:
            with open(filename, 'wb') as fp:
                fp.write(conn.content)
        else:
            print('Failed to request {url}'.format(url = url))
    else:
        os.system('wget --no-proxy --no-check-certificate {url}'.format(url = url))


def download_xwalk_android(branch, version, use_wget = False):
    '''
    Donwload the Crosswalk binary for Android from URL
    https://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/android/<BRANCH>/<VERSION>
    Content:
        <Version>/
        ├── arm/
        │   ├── crosswalk-apks-<VERSION>-arm.zip
        │   ├── crosswalk-test-apks-<VERSION>-arm.zip
        │   ├── crosswalk-webview-<VERSION>-arm.zip
        ├── arm64/
        │   ├── crosswalk-apks-<VERSION>-arm64.zip
        │   ├── crosswalk-test-apks-<VERSION>-arm64.zip
        │   ├── crosswalk-webview-<VERSION>-arm64.zip
        ├── crosswalk-<VERSION>-64bit.aar
        ├── crosswalk-<VERSION>-64bit.zip
        ├── crosswalk-<VERSION>.aar
        ├── crosswalk-<VERSION>.zip
        ├── crosswalk-shared-<VERSION>.aar
        ├── x86/
        │   ├── crosswalk-apks-<VERSION>-x86.zip
        │   ├── crosswalk-test-apks-<VERSION>-x86.zip
        │   ├── crosswalk-webview-<VERSION>-x86.zip
        └── x86_64/
            ├── crosswalk-apks-<VERSION>-x86_64.zip
            ├── crosswalk-test-apks-<VERSION>-x86_64.zip
            ├── crosswalk-webview-<VERSION>-x86_64.zip
    '''
    if branch == 'master':
        branch_name = 'canary'
    else:
        branch_name = branch

    version_dir = os.path.join(config.XWALK_BINARY_ANDROID_ROOT_DIR, branch, version)
    if not os.path.exists(version_dir):
        os.makedirs(version_dir)

    # Download arm/arm64/x86/x86_64
    for arch in config.ANDROID_ARCH:
        arch_dir = os.path.join(version_dir, arch)
        if not os.path.exists(arch_dir):
            os.mkdir(arch_dir)

        os.chdir(arch_dir)
        for arch_zip in config.ANDROID_ARCH_ZIP:
            arch_zip_name = arch_zip.format(version = version, arch = arch)
            if os.path.exists(os.path.join(arch_dir, arch_zip_name)):
                print('{zip} already exists!'.format(zip = arch_zip_name))
                continue

            arch_zip_url = urllib.parse.urljoin(config.URL_PREFIX,
                                                '/'.join(['crosswalk', 'android', branch_name, version,
                                                        arch, arch_zip_name])
                                                )
            download_file(arch_zip_url, arch_zip_name)

    os.chdir(version_dir)
    for xwalk_zip in config.ANDROID_ZIP:
        xwalk_zip_name = xwalk_zip.format(version = version)
        if os.path.exists(os.path.join(version_dir, xwalk_zip_name)):
            print('{zip} already exists!'.format(zip = xwalk_zip_name))
            continue

        xwalk_zip_url = urllib.parse.urljoin(config.URL_PREFIX,
                                                '/'.join(['crosswalk', 'android', branch_name, version,
                                                        xwalk_zip_name])
                                                )
        download_file(xwalk_zip_url, xwalk_zip_name, use_wget)


def download_xwalk_windows(branch, version, use_wget = False):
    '''
    Donwload the Crosswalk binary for Android from URL
    https://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/windows/<BRANCH>/<VERSION>
    Content:
        <VERSION>/
        crosswalk64-<VERSION>.zip
    '''
    if branch == 'master':
        branch_name = 'canary'
    else:
        branch_name = branch

    cts_dir = config.XWALK_BINARY_WINDOWS_DIRS.get(branch)
    if not cts_dir:
        sys.stderr.write('Check config.py, have you set the XWALK_BINARY_WINDOWS_DIRS correctly?')
        sys.exit(1)

    tools_dir = os.path.join(cts_dir, 'tools')
    os.chdir(tools_dir)

    for xwalk_zip in config.WINDOWS_ZIP:
        xwalk_zip_name = xwalk_zip.format(version = version)
        if os.path.exists(os.path.join(tools_dir, xwalk_zip_name)):
            print('{zip} already exists!'.format(zip = xwalk_zip_name))
            continue

        xwalk_zip_url = urllib.parse.urljoin(config.URL_PREFIX,
                                                '/'.join(['crosswalk', 'windows', branch_name, version,
                                                        xwalk_zip_name])
                                                )
        download_file(xwalk_zip_url, xwalk_zip_name)        



def download_xwalk_linux(version, branch = 'canary', use_wget = False):
    '''
    Donwload the Crosswalk binary for Android from URL
    https://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/linux/deb/canary/<VERSION>
    Content:
        <VERSION>/
        crosswalk_22.52.557.0-1_amd64.deb
        crosswalk_22.52.557.0-1_i386.deb
    '''
    version_dir = os.path.join(config.XWALK_BINARY_LINUX_ROOT_DIRS, branch, version)
    if not os.path.exists(version_dir):
        os.makedirs(version_dir)

    os.chdir(version_dir)
    for xwalk_deb in config.LINUX_DEB:
        xwalk_deb_name = xwalk_deb.format(version = version)
        if os.path.exists(os.path.join(version_dir, xwalk_deb_name)):
            print('{deb} already exists!'.format(deb = xwalk_deb_name))
            continue
        xwalk_deb_url = urllib.parse.urljoin(config.URL_PREFIX,
                                                '/'.join(['crosswalk', 'linux', 'deb', branch, version,
                                                        xwalk_deb_name])
                                            )
        download_file(xwalk_deb_url, xwalk_deb_name, use_wget)



if __name__ == '__main__':
    # download_xwalk_android('canary', '22.52.557.0')
    download_xwalk_linux('22.52.557.0')