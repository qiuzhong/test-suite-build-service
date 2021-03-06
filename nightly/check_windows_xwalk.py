#!/usr/bin/env python3


import sys
import check_xwalk



def check(branch):
    if branch == 'canary' or branch == 'master':
        check_xwalk.check_if_has_new_xwalk_for_windows_canary()
    elif branch == 'beta21':
        check_xwalk.check_if_has_new_xwalk_for_windows_beta21()
    elif branch == 'beta22':
        check_xwalk.check_if_has_new_xwalk_for_windows_beta22()		
    else:
        sys.stderr.write('Not supported branch for Windows')
        sys.exit(1)


if __name__ == '__main__':
    check(sys.argv[1])

