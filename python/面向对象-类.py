# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-04 17:51   #2024/10/4 17:51
@File：面向对象-类.PY
@IDE：PyCharm
@Motto：南风知我意
"""
class Player(object): #object 基类
    def __init__(self):
        pass

a = Player() # 类的实例化（创建对象）
print(type(a))
print(isinstance(a, Player))  #判断对象a是否是Player类的对象