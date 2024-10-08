# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-08 14:07   #2024/10/8 14:07
@File：test.PY
@IDE：PyCharm
@Motto：南风知我意
"""
def outer(func):
    def inner():
        print('我要开始睡觉了')
        func()
        print('我睡醒了')
    return inner


def sleep():
    print('睡觉中zZZZ')
sleep()