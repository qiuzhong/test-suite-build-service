#!/usr/bin/env python3

import os


version_file_names = [
	"beta20_version.txt",	
	"beta21_version.txt",
	"canary_version.txt"
]

pwd = os.getcwd()

def gen_version_files():
	for version_file in version_file_names:
		if not os.path.exists(os.path.join(pwd, version_file)):
			with open(version_file, 'w') as fp:
				fp.write('0.0.0.0')
		

if __name__ == '__main__':
	gen_version_files()