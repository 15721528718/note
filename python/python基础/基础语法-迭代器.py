# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-13 18:00   #2024/10/13 18:00
@File：基础语法-装饰器.PY
@IDE：PyCharm
@Motto：南风知我意
"""
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：iterator
# 生成器就是一个迭代器
# 常见的可迭代对象：
#   1.生成器
#   2.列表、元组、字典、字符串
# 列表、元组、字典、字符串虽然是可迭代对象，但不是迭代器，通过next取值会报错
# 将可迭代对象转换成迭代器
list1 = [12,23,24,34,56,'sade']
g = iter(list1)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))