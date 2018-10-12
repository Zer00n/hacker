#!/usr/bin/env python
#coding:utf-8
 
import urllib2
import urllib
import cookielib
import requests
import re
import sys
import threading
 
reload(sys)
sys.setdefaultencoding('utf8')
global titles
 
#加载页面内容
def load_page(url):

    try:
        httpproxy_handler = urllib2.ProxyHandler({"http" : "127.0.0.1:1087"})
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, httpproxy_handler)
        urllib2.install_opener(opener)
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"
        headers = {"User-Agent" : user_agent}
        postData = {
            ####抓包post到from的信息，账户密码等
            }
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl, postData, headers)
        response = urllib2.urlopen(request)
        html = response.read() 
        htmlc = html.decode("big5").encode("utf-8")
        h = urllib2.urlopen(url)
        htmlurl = h.read()
        htmlurl2 = htmlurl.decode("big5").encode("utf-8")    ##转码

        #print htmlurl2
        #print h.getcode()   #状态码
        print h.geturl()    #URL地址
        #print "--------------------------"
        getTitle(htmlurl2)
    except Exception,e:
        print str(e)
 
def tieba_spider(url,startPage,endPage):
    for i in range(startPage,endPage + 1):
        page = (i - 1) * 1
        my_url = url + str(page)
        load_page(my_url)
        print "--------第%d个----------" % i
 
def getTitle(htmlurl2):
    global titles
    info = re.findall(r'<td class="bold" width="65%">(.*?)</td>',htmlurl2,re.S)
    for titleList in info:
        print titleList
        print "---------------"
    titles.write(" ".join(info))
 
if __name__ == '__main__':
    posturl = 'http://login'    ####登陆from的地址
    url = "http://id"           ####需要爬取帖子的地址
    startPage = 111111
    endPage = 99999
    global titles 
    titles = open('tt.txt','w')
    tieba_spider(url, startPage, endPage)
    titles.close()
    print "---------------------结束------------------"
