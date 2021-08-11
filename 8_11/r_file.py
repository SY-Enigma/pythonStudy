# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 15:59
# @Author  : suyang
# @FileName: r_file.py
# @Software: PyCharm


# 打开一个文件
f = open("su.txt", "w",encoding="utf-8")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

print("写入完成！！！！！！！！！！！！！！！\n")

# 打开一个文件
f = open("su.txt", "r",encoding="utf-8")

str = f.read()
print(str)

# 关闭打开的文件
f.close()