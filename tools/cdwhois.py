#!/usr/bin/python
import re
import os

gfile = 'pac.txt'

def cwho(domain):
    cmd = '''dig %s ns @8.8.8.8 |grep -v "^;" |grep -v "^$" |grep 'IN\tSOA' > /dev/null''' % domain
    dig = os.system(cmd)
    if dig:
        #print domain,'ok'
        pass
    else:
        print(domain)

def main():
    f = open(gfile)
    for i in f.readlines():
        a = re.search('''"(.+)": 1,''',i)
        if a:
            d = a.group(1)
            cwho(d)
    f.close()

main()



'''
for i in `cat del.txt`; do echo  sed -ip "/$i/d" pac.txt ;done
'''


