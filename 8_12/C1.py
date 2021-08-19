# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 13:31
# @Author  : suyang
# @FileName: 装饰器.py
# @Software: PyCharm

# 可变参数

# 求平方和
def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)
squsum(1,2,3,4)