#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

from subprocess import Popen

devnull = open(os.devnull, 'wb')

ipscanner_ico = '''
#########################################################
#                     IP SCANNER                        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : Zer0_0n!                     #                       
#          Mail Address : evlove@163.com                #
#########################################################
'''

print ipscanner_ico

star = "**********************************************************************"

print star

ip_araligi_deger = raw_input("输入 IP 段 ( example: 192.168.0 ) ---> ")

print star

print "扫描的ip范围 ",ip_araligi_deger 

print star

if ip_araligi_deger == "":
 print star
 print "尝试有效的ip设备..."
 print star



p = []
aktif = 0
yanit_yok = 0
pasif = 0

for aralik in range(1,254):
    ip = ip_araligi_deger + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s 在线' % ip)
                aktif = aktif + 1
                aktif1 = aktif
            elif proc.returncode == 2:
                print('%s 无应答' % ip)
                aktif = yanit_yok + 1
            else:
                print('%s Pasif' % ip)
                pasif = pasif + 1
    time.sleep(.04)

devnull.close()
print star

print "LOCAL NETWORK IP SCANNER. By Zer0_0n!."

print star

#import os

print "当前的操作系统",os.name
print "扫描结果"
print "在线IP  [ ",aktif1," ]"
#print "被动IP [ ",pasif," ]"
#print "无应答  [ ",yanit_yok1," ]"

print star

bitis_mesaj = "扫描完成.."

print bitis_mesaj

print star
