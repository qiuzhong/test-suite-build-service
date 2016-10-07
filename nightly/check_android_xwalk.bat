cd C:\xwalk\release\test-suite-build-service\nightly
"C:\Python35\python.exe" check_android_xwalk.py %1
"C:\Python35\python.exe" mail.py Android %1