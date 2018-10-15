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
        httpproxy_handler = urllib2.ProxyHandler({"http" : "127.0.0.1:1087"})    #本机开机的SS代理
        cj = cookielib.LWPCookieJar()                                            #创建保存cookie的对象
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, httpproxy_handler)         #在使用urllib2访问url时，加入SS代理
        urllib2.install_opener(opener)
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"
        headers = {"User-Agent" : user_agent}
        postData = {
                #post的数据，通过burp抓包得知
            }
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl, postData, headers)
        response = urllib2.urlopen(request)
        html = response.read() 
        htmlc = html.decode("big5", 'ignore').encode("utf-8")   #出现big5转码错误，使用ignore忽略爆出的错误编码，直接以ASCII输出即可。
        h = urllib2.urlopen(url)
        htmlurl = h.read()
        htmlurl2 = htmlurl.decode("big5", 'ignore').encode("utf-8")

        #print htmlurl2
        print h.getcode()   #状态码
        print h.geturl()    #URL地址
        #print "--------------------------"
        getTitle(htmlurl2)
    except Exception,e:
        print str(e)
#循环
def tieba_spider(url,startPage,endPage):
    for i in range(startPage,endPage + 1):
        page = (i - 1) * 1
        my_url = url + str(page)
        load_page(my_url)
        print "%d--------------------" % i
 
def getTitle(htmlurl2):
    global titles
    info = re.findall(r'通过正则表达式，抓取页面中想抓取的信息',htmlurl2,re.S)
    for titleList in info:
        print titleList
        #print "---------------"
    titles.write(" ".join(info)+"\n")
 
if __name__ == '__main__':
    posturl = 'post到服务器login的url'
    url = "想爬取遍历的id="
    startPage = 1111
    endPage = 9999
    global titles 
    titles = open('写入本地文件.txt','w')
    tieba_spider(url, startPage, endPage)
    titles.close()
    print "---------------------结束------------------"
