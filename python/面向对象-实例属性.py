# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-04 17:51   #2024/10/4 17:51
@File：面向对象-类.PY
@IDE：PyCharm
@Motto：南风知我意
"""
class Player(object):
    def __init__(self,name,age,city): #初始化函数
        self.name = name
        self.age = age
        self.city = city

a = Player('xiaoming',18,'shenzhen')
print(a.age)
a.age=20
print(a.age)
print(a.__dict__)  # 获取一个对象的所有属性