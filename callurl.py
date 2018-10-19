#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import requests
import time

url = 'http://url'
fout = open('result.txt', 'w')
for i in range(300):
    r=requests.post(url)
    fout.write(url+' ： OK withstatus_code: '+str(r.status_code))
    print time.strftime('%H:%M:%S',time.localtime(time.time()))
    print(url+' ： OK withstatus_code: '+str(r.status_code))
fout.close()
