# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-08 14:07   #2024/10/8 14:07
@File：test.PY
@IDE：PyCharm
@Motto：南风知我意
"""
# def outer(func):
#     def inner():
#         print('我要开始睡觉了')
#         func()
#         print('我睡醒了')
#     return inner
#
#
# def sleep():
#     print('睡觉中zZZZ')
# sleep()
# a = outer(sleep)
# print(a())
"""
闭包是一个相对高级且功能强大的概念，它允许你保留函数的状态。

一、什么是闭包
闭包指的是满足以下几个条件的函数：

1.必须有一个内嵌函数。
2.内嵌函数必须引用外部函数中的变量。
3.外部函数的返回值必须是内嵌函数。

简而言之，闭包就是由函数以及创建该函数时存在的自由变量组成的实体。
1.示例测试
def counter():
    count = [0]
    def increment():
        count[0] += 1
        return count[0]
    return increment
my_counter = counter()
print(my_counter())
print(my_counter())
按照如上写法，第一个内部函数定义完成之后，外部函数进行return了，那么就不会走后边的内部函数了。
如何能实现两个函数都走呢，后边将给出示例。

二、闭包的作用
闭包主要有以下几个作用：
数据封装：闭包可以用于封装私有数据，只暴露有限的接口供外界访问。
保持变量状态：闭包允许函数记住和访问其词法作用域中的变量，即使函数在其作用域之外执行。
延迟计算：通过闭包可以推迟计算的执行，直到真正需要结果时。

三、闭包的使用场景
闭包常见的使用场景包括：
装饰器：在不修改原有函数代码的情况下，增加额外的功能。
回调函数：封装了状态的函数可以作为回调函数传递给某些操作。
函数工厂：根据输入参数的不同返回不同行为的函数。

四、闭包语法规范
要创建闭包，需要遵循以下语法规范：
定义外部函数。
在外部函数内定义内部函数。
内部函数引用外部函数的变量。
外部函数返回内部函数。

1.基础闭包
def outer_function(msg):
    # 外部函数的变量
    message = msg

    # 内部函数
    def inner_function():
        # 内部函数使用了外部函数的变量
        print(message)

    # 外部函数返回内部函数
    return inner_function

# 创建闭包实例
my_func = outer_function("Hello, World!")
# 调用内部函数
my_func()

outer_function是外部函数，它接受一个参数msg并将其赋值给局部变量message。
inner_function是内部函数，它访问了外部函数的局部变量message。
最后，outer_function返回了inner_function，但没有执行它（即没有使用inner_function()）。
当outer_function被调用并赋值给my_func时，它实际上返回了一个inner_function的实例，这个实例记住了message
的值，即使在outer_function执行完毕之后。

2.带有参数和操作的闭包
闭包也可以进行更复杂的操作，比如下面的例子展示了如何使用闭包来创建一个简单的计数器函数，该计数器可以增加或减少数值。
def counter(initial_value=0):
    count = [initial_value]  # 使用列表来存储计数值，以便在内部函数中修改

    def increment():
        # 增加计数
        count[0] += 1
        return count[0]

    def decrement():
        # 减少计数
        count[0] -= 1
        return count[0]

    # 返回两个内部函数
    return increment, decrement

# 创建闭包实例
inc, dec = counter(10)

# 使用闭包
print(inc())  # 输出: 11
print(dec())  # 输出: 10

counter函数根据初始值创建了一个计数器。
它定义了两个内部函数：increment和decrement，这两个函数都能够修改外部函数counter中的count列表。
通过返回这两个内部函数，我们可以创建具有特定初始值的计数器，并且可以独立地增加或减少计数值。

五、闭包代码示例
下面是一个简单的闭包示例，演示如何使用闭包来创建一个简单的计数器。
def counter(start=0):
    count = [start]
    
    def increment():
        count[0] += 1
        return count[0]
    
    return increment

# 创建一个从1开始计数的计数器
my_counter = counter(1)

print(my_counter())  # 输出: 2
print(my_counter())  # 输出: 3
counter函数是外部函数
increment是内部函数
increment函数引用了counter函数作用域中的count变量，并且counter函数返回了increment函数。这样，即使counter函数
的执行已经结束，increment函数仍然可以访问和修改count变量。
————————————————
                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/qq_35716085/article/details/136027158
"""
# def counter():
#     count = [0]
#     def increment():
#         count[0] += 1
#         return count[0]
#     return increment
# my_counter = counter()
# # print(my_counter())
# # print(my_counter())
#
# a = 0
# def aa():
#     a = 1
#     a += 2
#     print(a)
# aa()
