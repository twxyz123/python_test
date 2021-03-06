
# -*- coding: cp936 -*-
#题目：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
#这里统计包括目录下面的子目录
#包括空行和注释，但是要分别列出来
#这里是以C C++文件的注释来算的

import re
import os

#formatList = ['.h', '.H', '.c', '.C', '.cpp', 'CPP']
formatList = [".h", ".H", ".c", ".C", ".cpp", "CPP"]
allL=0
allS=0
allN=0
#计算filename文件有多少行， 有多少行空格，有多少行注释
def getFileLines(fileName):
    countL = 0
    countS = 0
    countN = 0
    flag = 0
    fi = open(fileName, 'r')
    for line in fi:
        #下面这两空行表达是一样的
        #if line.split() == []:
        if not re.findall("\S", line): 
            countS += 1
        #这里查找'//'情况的注释，这里如果是在代码后面的注释不单独算作一行
        elif (re.match("//", line) or re.match("[\s]+//", line)):
            #print '//---', countL
            countN += 1
        #下面两个判断分别来查找'/*','*/'，可能存在嵌套注释，所以这里用了一个列表
        else:
            #这个是为了这一行出现/***//**的情况
            leftN = line.count("/*")
            rightN = line.count("*/")
            if  leftN> rightN:
                #print '/*---', countL
                flag += 1
            if rightN > leftN:
                #print '*/---', (countL, leftN, rightN)
                flag -= 1
                countN += 1
        countL += 1;
        if 0 != flag:
            countN += 1
    return (countL, countS, countN)

def getPathFileLines(fpath):
    global allL, allS, allN
    files = os.listdir(fpath)
    for f in files:
        sf = fpath + '/' + f
        if os.path.isdir(sf): #如果是个文件夹，继续找里面的文件，这是一个回调
            getPathFileLines(sf)
        elif os.path.isfile(sf):
            #if os.path.splitext(f)[1] in formatList:
            array = map(f.endswith, formatList)
            if True in array:
                (countL, countS, countN) = getFileLines(sf)
                allL += countL
                allS += countS
                allN += countN
    return (allL, allS, allN)
    
#主函数
if __name__ == '__main__':
    #(countL, countS, countN) = getFileLines('E:/sunyun_my/ACWdx/AC_WDX_2010_pubnet_liuzzg/VASource/vsource/FFScale.cpp')
    #print '当前文件行数总数:%d,空行:%d,注释行:%d' % (countL, countS, countN)
    (countL, countS, countN) = getPathFileLines('E:\sunyun_my\ACWdx\AC_WDX_2010_pubnet_liuzzg')
    print '当前文件夹里的代码行数总数:%d,空行:%d,注释行:%d' % (countL, countS, countN)
    #print '当前文件夹里的代码行数总数:%d,空行:%d,注释行:%d' % (allL, allS, allN)
    print 'sucess!'
