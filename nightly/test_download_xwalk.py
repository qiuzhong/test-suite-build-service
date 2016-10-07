#!/usr/bin/env python3

import os
import sys
import shutil
import unittest

import config
import latest_ver
import download_xwalk


class TestDownloadXWalk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if sys.platform == 'linux':
            if not os.path.exists(config.XWALK_BINARY_ANDROID_ROOT_DIR):
                os.mkdir(config.XWALK_BINARY_ANDROID_ROOT_DIR)
            if not os.path.exists(config.XWALK_BINARY_LINUX_ROOT_DIRS):
                os.mkdir(config.XWALK_BINARY_LINUX_ROOT_DIRS)        


    @unittest.skipIf(sys.platform.startswith('win'), 'Linux platform only')
    def test_download_xwalk_android_canary(self):
        canary_version = latest_ver.LatestAndroidVersion.get('canary')
        download_xwalk.download_xwalk_android('canary', canary_version, use_wget = True)
        for android_zip in config.ANDROID_ZIP:
            abs_zip = os.path.join(config.XWALK_BINARY_ANDROID_ROOT_DIR, 'canary', 
                                    canary_version, android_zip.format(version = canary_version))
            self.assertTrue(os.path.exists(abs_zip))

        for arch in config.ANDROID_ARCH:
            for arch_zip in config.ANDROID_ARCH_ZIP:
                abs_arch_zip = os.path.join(config.XWALK_BINARY_ANDROID_ROOT_DIR, canary_version, 
                                            arch, arch_zip.format(version = canary_version, arch = arch))
                self.assertTrue(os.path.exists(abs_zip))


    @unittest.skipIf(sys.platform.startswith('win'), 'Linux platform only')
    def test_download_xwalk_android_beta(self):
        beta_version = latest_ver.LatestAndroidVersion.get('beta')
        download_xwalk.download_xwalk_android('beta', beta_version, use_wget = True)
        for android_zip in config.ANDROID_ZIP:
            abs_zip = os.path.join(config.XWALK_BINARY_ANDROID_ROOT_DIR, 'beta', 
									beta_version, android_zip.format(version = beta_version))
            self.assertTrue(os.path.exists(abs_zip))

        for arch in config.ANDROID_ARCH:
            for arch_zip in config.ANDROID_ARCH_ZIP:
                abs_arch_zip = os.path.join(config.XWALK_BINARY_ANDROID_ROOT_DIR, beta_version, 
                                            arch, arch_zip.format(version = beta_version, arch = arch))
                self.assertTrue(os.path.exists(abs_zip))


    @unittest.skipIf(sys.platform.startswith('win'), 'Linux platform only')
    def test_download_xwalk_linux_canary(self):
        canary_version = latest_ver.LatestLinuxVersion.get('canary')
        download_xwalk.download_xwalk_linux(canary_version, use_wget = True)
        for linux_deb in config.LINUX_DEB:
            abs_linux_deb = os.path.join(config.XWALK_BINARY_LINUX_ROOT_DIRS, 'canary', 
										canary_version, linux_deb.format(version = canary_version))
            self.assertTrue(os.path.exists(abs_linux_deb))


    @unittest.skipUnless(sys.platform.startswith('win'), 'Windows platform only')
    def test_download_xwalk_windows_canary(self):
        canary_version = latest_ver.LatestWindowsVersion.get('canary')
        download_xwalk.download_xwalk_windows('canary', canary_version)
        for windows_zip in config.WINDOWS_ZIP:
            abs_zip = os.path.join(config.XWALK_BINARY_WINDOWS_DIRS.get('canary'), 'tools',
                                    windows_zip.format(version = canary_version))
            self.assertTrue(os.path.exists(abs_zip))


    @unittest.skipUnless(sys.platform.startswith('win'), 'Linux platform only')
    def test_download_xwalk_windows_beta(self):
        beta_version = latest_ver.LatestWindowsVersion.get('beta')
        download_xwalk.download_xwalk_windows('beta21', beta_version)
        for windows_zip in config.WINDOWS_ZIP:
            abs_zip = os.path.join(config.XWALK_BINARY_WINDOWS_DIRS.get('beta21'), 
                                    'tools', windows_zip.format(version = beta_version))
            self.assertTrue(os.path.exists(abs_zip))


    @classmethod
    def tearDownClass(cls):
        if sys.platform == 'linux':
            if os.path.exists(config.XWALK_BINARY_ANDROID_ROOT_DIR):
                shutil.rmtree(config.XWALK_BINARY_ANDROID_ROOT_DIR)
            if os.path.exists(config.XWALK_BINARY_LINUX_ROOT_DIRS):
                shutil.rmtree(config.XWALK_BINARY_LINUX_ROOT_DIRS)
        elif sys.platform.startswith('win'):
            if os.path.exists(os.path.join(config.XWALK_BINARY_WINDOWS_DIRS.get('canary'), 'tools',
                                        'crosswalk64-{version}.zip'.format(
                                        version = latest_ver.LatestWindowsVersion.get('canary')))):
                print('dummy: removing crosswalk64-{version}.zip'.format(
                                        version = latest_ver.LatestWindowsVersion.get('canary')))
            if os.path.exists(os.path.join(config.XWALK_BINARY_WINDOWS_DIRS.get('beta21'), 'tools',
                                        'crosswalk64-{version}.zip'.format(
                                        version = latest_ver.LatestWindowsVersion.get('beta')))):
                print('dummy: removing crosswalk64-{version}.zip'.format(
                                        version = latest_ver.LatestWindowsVersion.get('beta')))            


if __name__ == '__main__':
    unittest.main()