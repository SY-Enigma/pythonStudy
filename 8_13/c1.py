# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 12:12
# @Author  : suyang
# @FileName: c1.py
# @Software: PyCharm
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
