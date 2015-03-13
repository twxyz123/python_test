
# -*- coding: cp936 -*-
#题目：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
#iPhone5分辨率:1136×640

import Image
import os

#原宽高sw， sh， 根据目标宽高w,h缩放
#按原比例缩放在w,h以内
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

#把fpath目录下的图片转成w，h以内的图片,保存在dpath目录下
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
        




#主函数
if __name__ == '__main__':
    reSizeImg('jpg', 'djpg', 1136, 640)
    print 'sucess!'
