# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 15:34
# @Author  : suyang
# @FileName: C2.py
# @Software: PyCharm

#  类 ，对象

# class Student():
#     name = ''
#     age = 0
#
#     def print_file(self):
#         print('name: ' +self.name)
#         print("age : " +str(self.age))
# student = Student()
# student.print_file()

# 实例化


class Student():
    name = ''
    age = 0

    def __init__(self):
        pass

    def print_file(self):
        print('name: ' +self.name)
        print("age : " +str(self.age))
student = Student()
student.print_file()
