
# -*- coding: cp936 -*-
#题目：做为 Apple Store App 独立开发者，你要搞限时促销，
#为你的应用生成激活码（或者优惠券），
#使用 Python 如何生成 200 个激活码（或者优惠券）

import random

#生成n位随机数字作为激活码
def generateCode(n):
    code = ''
    for i in range(0, n):
        a = random.randint(0, 9)
        code += str(a)
    return code

#生成m个n位的激活码，保存在fname文件中
def CodeWrite(fname, m, n):
    f = file(fname, 'w')
    for i in range(0, m):
        code = generateCode(n)
        code += '\r\n'
        f.write(code)
    f.close()


CodeWrite('code.txt', 200, 12)
print 'code generate sucess!'
