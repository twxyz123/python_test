# -*- coding: cp936 -*-
#��Ŀ:��һ��Ӣ�ĵĴ��ı��ļ���ͳ�����еĵ��ʳ��ֵĸ���

import re

#����fname�ļ��ĵ�������,���ݿո��������㵥����
#���Ӧ�ò�׼ȷ����ʱ���β��'.',','֮��ı�����
def countWord(fname):
    f = open(fname, 'r')
    text = f.read()
    alist = text.split(' ')
    num = len(alist)
    f.close()
    return num

#����fname�ļ��ĵ�������,����������ʽ���㵥����
#������ʽ��r'[a-zA-Z]+'
def countWord2(fname):
    f = open(fname, 'r')
    text = f.read()
    words1 = re.findall(r'[a-zA-Z]+',text);   #���������ʽ
    num = len(words1)
    f.close()
    return num

def countWord3(fname, word):
    f = open(fname, 'r')
    text = f.read()
    words1 = re.findall(word,text);   #���������ʽ
    num = len(words1)
    f.close()
    return num


#������
if __name__ == '__main__':
	print countWord2('dream.txt')
	#print countWord3('dream.txt', 'dream')
        #print countWord('dream.txt')
        
