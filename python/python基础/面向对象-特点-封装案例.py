# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-07 10:14   #2024/10/7 10:14
@File：面向对象-特点-多态.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
设计一个手机类，内容包含：
私有成员变量：__is_5g_enable. 类型bool。Ture表示开启5g，False表示关闭5g
私有成员方法：__check_5g(). 会判断私有成员is_5g_enable的值
若为Ture，打印输出：5g开始。
若为False，打印输出：5g关闭，使用4g网络
公开成员方法：call_by_5g() ，调用它会执行
调用私有成员方法：__check_5g()，判断5g网络状态
打印输出：正在通话中
通过完成这个类的设计和使用，体会封装中私有成员的作用
对用户公开的：call_by_5g()方法
对用户隐藏的：is_5g_enable私有变量和__check_5g私有成员
"""
class Phone:
    def __init__(self):
        self.__is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开始")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
p1 = Phone()
p1.call_by_5g()
