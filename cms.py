#!/usr/bin/python  
# -*- coding:utf8 -*-  
  
import os
allFileNum = 0
def printPath(level, path):
    global allFileNum
    dirList = []
    fileList = []
    files = os.listdir(path)
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            if(f[0] == '.'):
                pass
            else:
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            fileList.append(f)
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            dls = os.path.abspath(dl)
            print dls
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        print fl
        allFileNum = allFileNum + 1

if __name__ == '__main__':
    printPath(1, '/Users/leealex/python')
    print '总文件数 =', allFileNum
