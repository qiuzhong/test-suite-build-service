cd C:\xwalk\release\test-suite-build-service\nightly
"C:\Python35\python.exe" check_windows_xwalk.py %1
"C:\Python35\python.exe" mail.py Windows %1