# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 13:14
# @Author  : suyang
# @FileName: 装饰器.py
# @Software: PyCharm

#  装饰器@property

class Rect:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    @property
    def area(self):
         return self.width*self.height
rect = Rect(80,60)
print("面积为： ",rect.area)