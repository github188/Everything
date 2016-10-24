#!/usr/bin/env python

import urllib2
import time
import socket
import ssl
import time
from datetime import date

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

date_need = "2016-01-01"
content_date_ok = []

Mon_sum = 0
Tue_sum = 0
Wed_sum = 0
Thu_sum = 0
Fri_sum = 0

market = 'SZ'
code = '399006'
local_timeout = 3
url = 'http://xueqiu.com/S/' + market + str(code) + '/historical.csv'
req = urllib2.Request(url, headers = hdr)
content = urllib2.urlopen(req, timeout = local_timeout).read()
content = content.replace('"', '')
content_delete_first_line = '\n'.join(content.split('\n')[1:])
content_rstrip = content_delete_first_line.rstrip('\n')
print "result:"
#print content
content_list = content_rstrip.split('\n')
content_list_in_list = [x.split(',') for x in content_list]
for x in content_list_in_list:
    if x[1] > date_need:
        content_date_ok.append(x)
content_list_in_list = content_date_ok

if not content_list_in_list:
    exit
#print content_list_in_list
money = 10000
stock_num = 0
single_price = 0

for idx, x in enumerate(content_list_in_list):
    if (idx + 1) == len(content_list_in_list):
        break
    print x
    if ((float(x[5]) == 0) or (float(x[2]) == 0)):
        continue
    year, month, day = x[1].split("-")
    if (date(int(year), int(month), int(day)).weekday() == 0):
       Mon_sum += (float(x[5]) - float(x[2]))/float(x[2])
       print 'Mon'
       print Mon_sum
    if (date(int(year), int(month), int(day)).weekday() == 1):
       Tue_sum += (float(x[5]) - float(x[2]))/float(x[2])
       print Tue_sum
       if (stock_num != 0):
           money = stock_num * float(x[5])
           stock_num = 0
    if (date(int(year), int(month), int(day)).weekday() == 2):
       Wed_sum += (float(x[5]) - float(x[2]))/float(x[2])
       print Wed_sum
    if (date(int(year), int(month), int(day)).weekday() == 3):
       Thu_sum += (float(x[5]) - float(x[2]))/float(x[2])
       print Thu_sum
    if (date(int(year), int(month), int(day)).weekday() == 4):
       Fri_sum += (float(x[5]) - float(x[2]))/float(x[2])
       print Fri_sum
       if (stock_num == 0):
           stock_num = money/float(x[5])
           print stock_num

print '------------------'
print market + code
print 'start ' + '10000'
print 'end   ' + str(money)
