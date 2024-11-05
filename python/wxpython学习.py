# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-08 15:47   #2024/10/8 15:47
@File：wxpython学习.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from cProfile import label

import wx
def onClick(event):
    print('按钮被点击了')
# 创建应用程序对象
app = wx.App()
# 创建窗口
frm = wx.Frame(None,title='还得是你',size=(400,300),pos=(200,200))
# 显示窗口
frm.Show()
# 创建面板
pl = wx.Panel(frm,size=(300,200),pos=(100,100))
#显示面板
pl.Show()
# 创建静态文本
staticText = wx.StaticText(pl,label='你真行',pos=(50,10))
# 创建静态按钮
btn = wx.Button(pl,label='测试',pos=(100,50))
# 显示按钮
btn.Show()
# 给按钮绑定事件
frm.Bind(wx.EVT_BUTTON,onClick,btn)




# 进入主循环，让窗口一直显示
app.MainLoop()
