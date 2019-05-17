#!/bin/env python
#coding:utf-8


import requests
import sys
import os


url = "http://s1.edufe.com.cn/tophp/getStudentInfoForPHP?userId=qiqi"
r = requests.get(url, timeout=5)
text = r.text
#print  text
text2 = r.content
#print text2
code = r.status_code
#print code
text1 = {u'studykind': u'\u5355\u79d1\u9009\u4fee', u'studentname': u'\u742a\u742a', u'sch_level': u'', u'provincename': u'\u5c71\u897f\u7701', u'studykindid': u'b01', u'fdzjgcode': u'10173070', u'userid': u'qiqi', u'rx_level': u'200402', u'subjectid': u'03', u'sex': u'0', u'stu_level': u'200402', u'cityname': u'\u592a\u539f', u'cardid': u'312215454453811', u'fdzname': u'\u6d4b\u8bd5\u5b66\u4e60\u4e2d\u5fc3', u'subject': u'\u5355\u79d1\u9009\u4fee'}
#text1 = {"studentname":"琪琪","userid":"qiqi","sex":"0","cardid":"312215454453811","rx_level":"200402","stu_level":"200402","sch_level":"","studykind":"单科选修","studykindid":"b01","subject":"单科选修","subjectid":"03","fdzname":"测试学习中心","fdzjgcode":"10173070","provincename":"山西省","cityname":"太原"}

#print r.text

if text == '':
	os.system("python /usr/local/zabbix/share/zabbix/alertscripts/weixin2018.py Classroom error")
	sys.exit(1)
else:
	print"OK 访问最正常！"
	exit(2)
#print text2
#textr = r.json()
#print r.json()

#if textr == text1:
#	print "OK !"
#	sys.exit(0)
#else:
#	os.system("python /usr/local/zabbix/share/zabbix/alertscripts/weixin2018.py Classroom error")
#        sys.exit(2)
        
#if code == 200: 
#        print r.text
#	print "OK 网站访问正常"
#	sys.exit(0)
#else:
#	print "Error 不能访问！"
#	sys.exit(2)
