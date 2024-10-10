# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-03 16:04   #2024/10/3 16:04
@File：模块-turtle.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import turtle,time
pen = turtle.Turtle()
pen.speed(0)
# for i in range(500):
#     pen.forward(100+i)
#     pen.left(105)

pen.backward(100)
while True:
    t = time.localtime()
    pen.clear()
    pen.write(time.strftime('%Y-%m-%d %H:%M:%S',t),font=('Arial',24,'normal'))
    time.sleep(1)
    input()