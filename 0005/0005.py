
# -*- coding: cp936 -*-
#��Ŀ������һ��Ŀ¼��װ�˺ܶ���Ƭ�������ǵĳߴ��ɶ������� iPhone5 �ֱ��ʵĴ�С
#iPhone5�ֱ���:1136��640

import Image
import os

#ԭ���sw�� sh�� ����Ŀ����w,h����
#��ԭ����������w,h����
def reSizeWH(sw, sh, w, h):
    f1 = float(w) / float(sw)
    f2 = float(h) / float(sh)
    #print 'f1 %.3f, f1 %.3f' % (f1,f2)
    if (f1 >= 1 and f2 >= 1):
        dw = sw
        dh = sh
    elif (f1 <= f2):
        dw = sw * f1
        dh = sh * f1
    else :
        dw = sw * f2
        dh = sh * f2       
    return (int(dw), int(dh))

#��fpathĿ¼�µ�ͼƬת��w��h���ڵ�ͼƬ,������dpathĿ¼��
#dpath
def reSizeImg(fpath, dpath, w, h):
    files = os.listdir(fpath)
    for f in files:
        sf = fpath + '/' + f
        im = Image.open(sf)
        (x, y) = im.size
        (dw, dh) = reSizeWH(x, y, w, h)
        out = im.resize((dw, dh), Image.ANTIALIAS)
        df = dpath + '/' + f
        out.save(df)
        print'(%d, %d) --> (%d, %d)' %(x, y, dw, dh)
        




#������
if __name__ == '__main__':
    reSizeImg('jpg', 'djpg', 1136, 640)
    print 'sucess!'
