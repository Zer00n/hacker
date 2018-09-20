#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys
import urllib2
import threading
import Queue
q=Queue.Queue()

baidu_spider="Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"

lines=open("ASP11.txt",'r')
for line in lines:
    line=line.rstrip()
    q.put(line)



ipscanner_ico = '''
#########################################################
#                    BACK DOOR SCAN                     #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : Zer0_0n!                     #                       
#          Mail Address : evlove@163.com                #
#########################################################
'''

print ipscanner_ico


def scaner():
    while not q.empty():
        path=q.get()
        url="%s%s" % (domain_name,path)
        #print path
        headers={}
        headers['User-Agent']=baidu_spider
        requset=urllib2.Request(url,headers=headers)
        try:
            response = urllib2.urlopen(requset)
            content=response.read()
            if len(content):
                print "Status [%s] - path: %s" % (response.code,url)
                #wx('urlyes.txt',url+'\n')
            response.close()
        except urllib2.HTTPError as e:
            pass   
#def show():
#    print "hscan1.py http://URL 10"


def wx(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        #show()
        sys.exit()
    thread_num=sys.argv[2]
    domain_name=sys.argv[1]
    for i in range(int(sys.argv[2])): 
        t = threading.Thread(target=scaner)
        t.start()
        lines.close()
