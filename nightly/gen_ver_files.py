#!/usr/bin/env python3

import os

import config 


pwd = os.getcwd()

def gen_version_files(overwrite = False):
	version_file_list = list(config.XWALK_ANDROID_VERSION_FILE.values()) + list(config.XWALK_WINDOWS_VERSION_FILE.values())
	for version_file in version_file_list:
		if not os.path.exists(os.path.join(pwd, version_file)) or overwrite:
			with open(version_file, 'w') as fp:
				fp.write('0.0.0.0')
		
def gen_update_json_files(overwrite = False):
	version_file_list = list(config.XWALK_ANDROID_UPDATE_JSON_FILE.values()) + list(config.XWALK_WINDOWS_UPDATE_JSON_FILE.values())
	for version_file in version_file_list:
		if not os.path.exists(os.path.join(pwd, version_file)) or overwrite:
			with open(version_file, 'w') as fp:
				fp.write('')
				

if __name__ == '__main__':
	# gen_version_files()
	gen_update_json_files