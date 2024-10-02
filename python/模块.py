# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-09-30 19:00   #30/9/2024 PM7:00
@File：模块.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import random
# a = random.random()
# a = random.choice('hello')
#生成一个随机字母组成的列表
def random_list():
    a = []
    for i in range(10):
        chr_t = chr(random.randint(65,122))
        a.append(chr_t)
    return ''.join(a)
print(random_list())
"""
模块：
就好比是工具包，想要使用这个工具包中的模块，就需要导入import这个模块
每一个以扩展名py结尾的python源代码文件都是一个模块
在模块中定义的全局变量、函数都是模块能够提供给外界直接使用的工具

包的使用：
包是python模块的一种组织形式，将多个模块组合在一起，形成一个大的python工具库。
包通常是一个拥有__init__.py文件的目录，它定义了包的属性和方法。

常见的标准库：
os os模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
sys sys模块提供了与python解释器和系统相关的功能，例如解释器的版本和路径，以及与stdin、stdout和stderr相关的信息。
time time模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。
datetime datetime模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。
random random模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
math math模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。
re re模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
json json模块提供了json编码和解码函数，可以将python对象转换为json格式，并从json格式中解析出python对象。
urllib urllib模块提供了访问网页和处理url的功能，包括下载文件、发送post请求、处理cookies等。

"""
