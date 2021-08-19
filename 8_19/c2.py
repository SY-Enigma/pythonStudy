# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 15:47
# @Author  : suyang
# @FileName: c2.py
# @Software: PyCharm

import wx


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='dhhhhd')
        frame.Show()
        return True


if __name__== '__main__':
    app = App()
    app.MainLoop()
