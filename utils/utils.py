import os
import sys
import hashlib

def getMd5(file):
	m = hashlib.md5()
	while True:
		data = file.read(4096)
		if not data:
			break
		m.update(data)
	
	return m.hexdigest()

# if __name__ == '__main__':
# 	test_file = open('/root/guofen-web/main/index.html')
# 	print(getMd5(test_file))
