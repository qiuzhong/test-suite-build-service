import os


URL_PREFIX = "http://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk"

# XWALK_BINARY_ANDROID_ROOT_DIR = \
# os.path.expanduser("~/00_jiajia/images/linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/android")

XWALK_BINARY_ANDROID_ROOT_DIR = \
os.path.expanduser("~/01_qiuzhong/02-git/02-qz/test-suite-build-service/nightly/android")

XWALK_BINARY_WINDOWS_DIRS = {
    "canary": r"C:\xwalk\crosswalk-test-suite",
    "beta21": r"C:\xwalk\crosswalk-test-suite-21"
}

XWALK_BINARY_LINUX_ROOT_DIRS =  \
os.path.expanduser("~/01_qiuzhong/02-git/02-qz/test-suite-build-service/nightly/linux")

ANDROID_ARCH = (
    "arm",
    "arm64",
    "x86",
    "x86_64"
)

ANDROID_ARCH_ZIP = (
    "crosswalk-apks-{version}-{arch}.zip",
    "crosswalk-test-apks-{version}-{arch}.zip",
    "crosswalk-webview-{version}-{arch}.zip"
)

ANDROID_ZIP = (
    "crosswalk-{version}-64bit.aar",
    "crosswalk-{version}-64bit.zip",
    "crosswalk-{version}.aar",
    "crosswalk-{version}.zip",
    "crosswalk-shared-{version}.aar"
)

WINDOWS_ZIP = (
    "crosswalk64-{version}.zip",
)

LINUX_DEB = (
    "crosswalk_{version}-1_amd64.deb",
    "crosswalk_{version}-1_i386.deb"
)