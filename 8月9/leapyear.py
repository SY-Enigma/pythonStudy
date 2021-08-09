# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 14:07
# @Author  : suyang
# @FileName: leapyear.py
# @Software: PyCharm


# year = 2021
# result = "是闰年" if(year%4 == 0 and year %  100 != 0) or (year % 100 ==0) else "不是闰年"
# print("\n"+str(year) +"年"+result +"!")


year =int(input("请输入一个年份: "))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0 :
            print(year,"年是闰年")
        else:
            print(year,"年不是闰年")
    else:
         print(year,"年是闰年")
else:
    print(year,"年不是闰年")
