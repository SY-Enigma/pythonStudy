# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 14:09
# @Author  : suyang
# @FileName: FristGUI.py
# @Software: PyCharm


# 登录GUI

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(400, 300))
        panel = wx.Panel(self)
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)

        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)

        self.title = wx.StaticText(panel, label="请输入用户名与密码")
        self.lable_user = wx.StaticText(panel, label="用户名：")
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.table_pwd = wx.StaticText(panel, label="密  码：")
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 添加容器，容器中控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.lable_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)

        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.table_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件纵向排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.Top, border=15)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self,event):
        message = ""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        if username == "" or password == "":
            message = '用户名或密码不能为空'
        elif username == 'suyang' or password == '123456':
            message = '登录成功'
        else:
            message = '用户名和密码不匹配'
        wx.MessageBox(message)

    def OnclickCancel(self, event):
        self.text_user.SetValue("")
        self.text_password.SetValue("")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
