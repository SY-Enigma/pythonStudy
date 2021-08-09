# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 13:18
# @Author  : suyang
# @FileName: BMI.py
# @Software: PyCharm

height = float(input("请输入你的身高:    "))  # 米

weight = float(input("请输入你的体重:    "))  # KG
bmi = weight/(height*height)
#判断身材是否合理
if bmi < 18.5:
    print("你的BMI指数为："+str(bmi))
    print("体重过轻@@")
    if bmi >= 18.5 and bmi < 24.9:
        print("你的BMI指数为：" + str(bmi))
        print("正常范围，注意保持")
        if bmi >= 24.9 and bmi < 29.9:
            print("你的BMI指数为：" + str(bmi))
            print("体重过重")
            if bmi >= 29.9:
                print("你的BMI指数为：" + str(bmi))
                print("体重肥胖")