import os


URL_PREFIX = "http://linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk"

# XWALK_BINARY_ANDROID_ROOT_DIR = \
# os.path.expanduser("~/00_jiajia/images/linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/android")

XWALK_BINARY_ANDROID_ROOT_DIR = \
os.path.expanduser("~/01_qiuzhong/02-git/02-qz/test-suite-build-service/nightly/android")

XWALK_BINARY_WINDOWS_DIRS = {
    "canary": r"C:\xwalk\crosswalk-test-suite",
    "beta21": r"C:\xwalk\crosswalk-test-suite-21",
	"beta22": r"C:\xwalk\crosswalk-test-suite-22"
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

unzip_cmd = r'"C:\Program Files\2345Soft\HaoZip\HaoZipC.exe"'

XWALK_WINDOWS_VERSION_FILE = {	
	"beta20": "windows_beta20_version.txt",
	"beta21": "windows_beta21_version.txt",
	"beta22": "windows_beta22_version.txt",
	"canary": "windows_canary_version.txt"
}

XWALK_ANDROID_VERSION_FILE = {
    "beta20": "android_beta20_version.txt",
    "beta21": "android_beta21_version.txt",
	"beta22": "android_beta22_version.txt",
    "canary": "android_canary_version.txt"
}

XWALK_ANDROID_UPDATE_JSON_FILE = {
    "beta20": "android_beta20.json",
    "beta21": "android_beta21.json",
	"beta22": "android_beta22.json",
    "canary": "android_canary.json"
}

XWALK_WINDOWS_UPDATE_JSON_FILE = {
    "beta20": "windows_beta20.json",
    "beta21": "windows_beta21.json",
	"beta22": "windows_beta22.json",
    "canary": "windows_canary.json"
}
