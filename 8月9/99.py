# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 14:28
# @Author  : suyang
# @FileName: 99.py
# @Software: PyCharm

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) +"X" +str(i)+ "=" +str(i*j)+"\t",end="")
        print("")