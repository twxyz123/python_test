
# -*- coding: cp936 -*-
#��Ŀ����Ϊ Apple Store App ���������ߣ���Ҫ����ʱ������
#Ϊ���Ӧ�����ɼ����루�����Ż�ȯ����
#ʹ�� Python ������� 200 �������루�����Ż�ȯ��

import random

#����nλ���������Ϊ������
def generateCode(n):
    code = ''
    for i in range(0, n):
        a = random.randint(0, 9)
        code += str(a)
    return code

#����m��nλ�ļ����룬������fname�ļ���
def CodeWrite(fname, m, n):
    f = file(fname, 'w')
    for i in range(0, m):
        code = generateCode(n)
        code += '\r\n'
        f.write(code)
    f.close()


CodeWrite('code.txt', 200, 12)
print 'code generate sucess!'
