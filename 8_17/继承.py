# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 13:23
# @Author  : suyang
# @FileName: 继承.py
# @Software: PyCharm

class Fruit:
    color ="绿色"
    def harvest(self,color):
        print("水果是：" +color+"的")
        print("水果已经收获...........")
        print("水果原来是："+Fruit.color+"的！")
class Apple(Fruit):
    color = "红色"
    def __init__(self):
        print("苹果")
class Orange(Fruit):
    color = "橙色"
    def __init__(self):
        print("\n我是橘子")
apple = Apple()
apple.harvest(apple.color)
orange = Orange()
orange.harvest(orange.color)