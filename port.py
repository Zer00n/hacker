# -*- coding: utf-8 -*-
#!/usr/bin/python2
from socket import *
import threading
 
lock = threading.Lock()
openNum = 0
 
def portScanner(host,port):
  global openNum
  try:
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((host,port))
    lock.acquire()
    openNum+=1
    print('[+] %d open' % port)
    lock.release()
    s.close()
  except:
    pass
 
def main():

  ipscanner_ico = '''
#########################################################
#                     PORT SCANNER                        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : Zer0_0n!                     #                       
#          Mail Address : evlove@163.com                #
#########################################################
'''
  star = "**********************************************************************"

  print ipscanner_ico

  ip_araligi_deger = raw_input("输入 IP ( example: 192.168.0.1 ) ---> ")
  
  #if ip_araligi_deger == "":
  #print star
  #print "尝试有效的ip设备..."
  #print star


  setdefaulttimeout(1)
  for n in range(1,76):
    threads = []
    print (n-1)*880,n*880
    for p in range((n-1)*880,n*880):
      t = threading.Thread(target=portScanner,args=(ip_araligi_deger,p))
      threads.append(t)
      t.start()
 
    for t in threads:
      pass
    t.join()#在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
 
  print('[*] The scan is complete!')
  print('[*] A total of %d open port ' % (openNum))
 
if __name__ == '__main__':
  main()
