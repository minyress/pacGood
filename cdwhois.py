#!/usr/bin/env python
import re
import os

gfile = 'gfwlist.txt'

def cwho(domain):
	cmd = '''dig %s ns |grep "a.gtld-servers.net. nstld.verisign-grs.com." > /dev/null'''%domain
	dig = os.system(cmd)
	if dig:
		#print domain,'ok'
		pass
	else:
		print domain

def main():
	f = open(gfile)
	for i in f.readlines():
		a = re.search('''"(.+)": 1,''',i)
		if a:
			d = a.group(1)
			cwho(d)
	f.close()

main()
