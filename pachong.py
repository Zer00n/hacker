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
    '''
    发送url请求
    返回url请求的静态html页面
    :param url:
    :return:
    '''
    try:
        httpproxy_handler = urllib2.ProxyHandler({"http" : "127.0.0.1:1087"})
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, httpproxy_handler)
        urllib2.install_opener(opener)
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"
        headers = {"User-Agent" : user_agent}
        postData = {
            'formhash': '95d3049b',
            'referer': '',
            'cookietime': '2592000',
            'loginfield': 'username',
            'username': 'djjackol',
            'password': 'alex123qweasd',
            'questionid': '0',
            'answer': '',
            'loginsubmit': '會員登錄'
            }
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl, postData, headers)
        response = urllib2.urlopen(request)
        html = response.read() 
        htmlc = html.decode("big5").encode("utf-8")
        h = urllib2.urlopen(url)
        htmlurl = h.read()
        htmlurl2 = htmlurl.decode("big5").encode("utf-8")

        #print htmlurl2
        #print h.getcode()   #状态码
        print h.geturl()    #URL地址
        #print "--------------------------"
        getTitle(htmlurl2)
    except Exception,e:
        print str(e)
 
#生成url地址，加载页面内容
def tieba_spider(url,startPage,endPage):
    for i in range(startPage,endPage + 1):
        page = (i - 1) * 1
        my_url = url + str(page)
        load_page(my_url)
        print "--------第%d页----------" % i
 
#获得贴吧的标题
def getTitle(htmlurl2):
    global titles
    info = re.findall(r'<td class="bold" width="65%">(.*?)</td>',htmlurl2,re.S)
    for titleList in info:
        print titleList
        print "---------------"
    titles.write(" ".join(info))
 
if __name__ == '__main__':
    posturl = 'http://www.spring4u.info/logging.php?action=login'
    url = "http://www.spring4u.info/viewthread.php?tid="
    startPage = 131000
    endPage = 132000
    global titles 
    titles = open('tiebaTitles.txt','w')
    tieba_spider(url, startPage, endPage)
    titles.close()
    print "---------------------结束------------------"
