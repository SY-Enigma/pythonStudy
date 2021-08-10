# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 13:49
# @Author  : suyang
# @FileName: c1.py
# @Software: PyCharm

account = 'suyang'
password = '123456'


print("请输入用户名")
user_account = input()
print("请输入密码")
user_password = input()
if user_account == account and  user_password == password:
    print("success")
else:
    print("fail")