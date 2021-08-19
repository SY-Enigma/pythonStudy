# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 12:45
# @Author  : suyang
# @FileName: C2.py
# @Software: PyCharm


# 查看学生成绩

n = float(input("请输入成绩： "))
if n > 100 or n < 0:
    print("错误输入！！请正确输入")
elif 90 < n <= 100:
    print("A")
elif 80 < n < 90:
    print("B")
elif 70 <= n < 80:
    print("C")
elif 60 <= n < 70:
    print("D")
else:
    print("E")


