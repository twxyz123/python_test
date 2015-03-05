# -*- coding: cp936 -*-
#题目:任一个英文的纯文本文件，统计其中的单词出现的个数

import re

#计算fname文件的单词数量,根据空格数量计算单词量
#这个应该不准确，有时候结尾是'.',','之类的标点符合
def countWord(fname):
    f = open(fname, 'r')
    text = f.read()
    alist = text.split(' ')
    num = len(alist)
    f.close()
    return num

#计算fname文件的单词数量,根据正则表达式计算单词量
#正则表达式：r'[a-zA-Z]+'
def countWord2(fname):
    f = open(fname, 'r')
    text = f.read()
    words1 = re.findall(r'[a-zA-Z]+',text);   #这个正则表达式
    num = len(words1)
    f.close()
    return num

def countWord3(fname, word):
    f = open(fname, 'r')
    text = f.read()
    words1 = re.findall(word,text);   #这个正则表达式
    num = len(words1)
    f.close()
    return num


#主函数
if __name__ == '__main__':
	print countWord2('dream.txt')
	#print countWord3('dream.txt', 'dream')
        #print countWord('dream.txt')
        
