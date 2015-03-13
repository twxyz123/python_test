
# -*- coding: cp936 -*-
#��Ŀ���и�Ŀ¼�����������Լ�д���ĳ���ͳ��һ����д�������д��롣
#����ͳ�ư���Ŀ¼�������Ŀ¼
#�������к�ע�ͣ�����Ҫ�ֱ��г���
#��������C C++�ļ���ע�������

import re
import os

#formatList = ['.h', '.H', '.c', '.C', '.cpp', 'CPP']
formatList = [".h", ".H", ".c", ".C", ".cpp", "CPP"]
allL=0
allS=0
allN=0
#����filename�ļ��ж����У� �ж����пո��ж�����ע��
def getFileLines(fileName):
    countL = 0
    countS = 0
    countN = 0
    flag = 0
    fi = open(fileName, 'r')
    for line in fi:
        #�����������б����һ����
        #if line.split() == []:
        if not re.findall("\S", line): 
            countS += 1
        #�������'//'�����ע�ͣ�����������ڴ�������ע�Ͳ���������һ��
        elif (re.match("//", line) or re.match("[\s]+//", line)):
            #print '//---', countL
            countN += 1
        #���������жϷֱ�������'/*','*/'�����ܴ���Ƕ��ע�ͣ�������������һ���б�
        else:
            #�����Ϊ����һ�г���/***//**�����
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
        if os.path.isdir(sf): #����Ǹ��ļ��У�������������ļ�������һ���ص�
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
    
#������
if __name__ == '__main__':
    #(countL, countS, countN) = getFileLines('E:/sunyun_my/ACWdx/AC_WDX_2010_pubnet_liuzzg/VASource/vsource/FFScale.cpp')
    #print '��ǰ�ļ���������:%d,����:%d,ע����:%d' % (countL, countS, countN)
    (countL, countS, countN) = getPathFileLines('E:\sunyun_my\ACWdx\AC_WDX_2010_pubnet_liuzzg')
    print '��ǰ�ļ�����Ĵ�����������:%d,����:%d,ע����:%d' % (countL, countS, countN)
    #print '��ǰ�ļ�����Ĵ�����������:%d,����:%d,ע����:%d' % (allL, allS, allN)
    print 'sucess!'
