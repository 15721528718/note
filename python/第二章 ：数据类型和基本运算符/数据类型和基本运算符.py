# -*- coding: utf-8 -*-
'''
@Auth：bee
@Time：2024-09-27 15:35   #27/9/2024 PM3:35
@File：变量的定义和使用.PY
@IDE：PyCharm
@Motto：南风知我意
'''
# 1.保留字与标识符
# 2.理解python中的变量、定义及使用
# 3.基本数据类型
# 4.数据类型之间的转换
# 5.eval()函数
# 6.不同的进制数
# 7.运算符
# 8.运算符的优先级

# 变量的定义和使用
# 使用内置函数type()查看变量数据类型 id()查看指向的的内存地址
# 常量规定使用大写字母和下划线组成

# 浮点数类型_复数类型
# 保留4位小数
a= round(0.1203456,4)
# 复数类型
# x=a+bj
# j=√-1
# .real获取实数部分 .imag获取虚数部分
x=123+456j
"实数部分",x.real
"虚数部分",x.imag

"""
eval函数的使用
eval()函数 —eval(s)函数将去掉字符串s最外侧的引号，并按照python语句方式执行去掉引号后的字符串。
也可以这样来理解：eval()函数就是实现list、dict、tuple、与str之间的转化
"""
x = 7
eval( '3 * x' )
# 21
eval('pow(2,2)')
# 4
eval('2 + 2')
# 4
n=81
eval("n + 4")
# 85

"""
1、字符转换为列表：
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))
b = eval(a)
print(type(b))
print(b)

2、字符串转换为字典
a = "{1: 'a', 2: 'b'}"
print(type(a))b = eval(a)
print(type(b))
print(b)

3、字符转换为元组
a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(a))b=eval(a)
print(type(b))
print(b)

"""
