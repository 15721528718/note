# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-04 17:51   #2024/10/4 17:51
@File：面向对象-类.PY
@IDE：PyCharm
@Motto：南风知我意
"""
class Player(object):
    numbers = 0   # 类属性
    def __init__(self,name,age,city): #初始化函数
        self.name = name
        self.age = age
        self.city = city
        Player.numbers += 1

a = Player('xiaoming',18,'shenzhen')
b = Player('xiaohong',17,'shenzhen')
print(Player.numbers)