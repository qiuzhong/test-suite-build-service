#!/usr/bin/env python3

import sys
import urllib.parse

import requests
from bs4 import BeautifulSoup

import config


def get_request_url(url):
    conn = requests.get(url, verify = False)
    if not conn or not conn.content:
        sys.stderr.write('Failed to request {url}'.format(url = url))
        sys.exit(1)

    soup = BeautifulSoup(conn.content, 'html.parser')
    ver_links = soup.find_all('a')
    return ver_links


def detect_latest_android(branch):
    '''Detect the latest version of Crosswalk for Android from URL
    https://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/android/latest
    branch:
        stable
        beta
        canary/master
    content:
        arm/
        arm64/
        x86/
        x86_64/
        crosswalk-<VERSION>-64bit.aar
        crosswalk-<VERSION>-64bit.zip
        crosswalk-<VERSION>.aar
        crosswalk-<VERSION>.zip
        crosswalk-shared-<VERSION>.aar

    '''
    branch_name = None
    if branch == 'master':
        branch_name = 'canary'
    else:
        branch_name = branch

    latest_url = urllib.parse.urljoin(config.URL_PREFIX,
                                    '/'.join(['crosswalk', 'android', 
                                            branch_name, 'latest']
                                            )
                                    )
    links = get_request_url(latest_url)
    content = sorted([link.string for link in links 
                                if link.string != '../' and 
                                link.string.startswith('crosswalk')])
    version = content[-2].lstrip('crosswalk-').rstrip('.zip')
    return version


def detect_latest_windows(branch):
    '''Detect the latest version of Crosswalk for Windows from URL
    http://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/windows/latest
    branch:
        stable
        beta
        canary/master
    content:
        crosswalk64-22.52.557.0.zip
    '''
    branch_name = None
    if branch == 'master':
        branch_name = 'canary'
    else:
        branch_name = branch

    latest_url = urllib.parse.urljoin(config.URL_PREFIX,
                                    '/'.join(['crosswalk', 'windows', 
                                            branch_name, 'latest']
                                            )
                                    )
    links = get_request_url(latest_url)
    content = sorted([link.string for link in links 
                                if link.string != '../' and 
                                link.string.startswith('crosswalk')])
    version = content[0].lstrip('crosswalk64-').rstrip('.zip')
    return version


def detect_latest_linux():
    '''Detect the latest version of Crosswalk for Linux from URL
    http://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/linux/deb/canary/latest/
    branch:
        canary/master
    content:
        crosswalk_22.52.557.0-1_amd64.deb
        crosswalk_22.52.557.0-1_i386.deb
    '''
    latest_url = urllib.parse.urljoin(config.URL_PREFIX,
                                    '/'.join(['crosswalk', 'linux', 'deb',
                                            'canary', 'latest']
                                            )
                                    )
    links = get_request_url(latest_url)

    content = sorted([link.string for link in links 
                                if link.string != '../' and 
                                link.string.startswith('crosswalk')])
    version = content[0].lstrip('crosswalk_').rstrip('-1_amd64.deb')
    return version


if __name__ == '__main__':
    latest_android_ver = detect_latest_android('master')
    print(latest_android_ver)

    latest_windows_ver = detect_latest_windows('master')
    print(latest_windows_ver)

    latest_canary_ver = detect_latest_linux()
    print(latest_canary_ver)