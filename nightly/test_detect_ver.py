#!/usr/bin/env python3


import unittest

import gen_ver_files
import detect_ver
import latest_ver


class TestDetectXWalkVersion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        gen_ver_files.gen_version_files()


    def test_detect_android_canary_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_android('canary'), latest_ver.LatestAndroidVersion['canary'])
        self.assertEqual(detect_ver.detect_latest_android('master'), latest_ver.LatestAndroidVersion['canary'])

    def test_detect_android_beta_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_android('beta'), latest_ver.LatestAndroidVersion['beta'])

    def test_detect_android_stable_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_android('stable'), latest_ver.LatestAndroidVersion['stable'])
        
    def test_detect_windows_canary_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_windows('canary'), latest_ver.LatestWindowsVersion['canary'])
        self.assertEqual(detect_ver.detect_latest_windows('master'), latest_ver.LatestWindowsVersion['canary'])

    def test_detect_windows_beta_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_windows('beta'), latest_ver.LatestWindowsVersion['beta'])

    def test_detect_windows_stable_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_windows('stable'), latest_ver.LatestWindowsVersion['stable'])

    def test_detect_linux_stable_latest_ver(self):
        self.assertEqual(detect_ver.detect_latest_linux(), latest_ver.LatestLinuxVersion['canary'])        


if __name__ == '__main__':
    unittest.main()