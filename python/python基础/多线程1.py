# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-15 16:13   #2025/4/15 16:13
@File：多线程.PY
@IDE：PyCharm
@Motto：南风知我意
"""

print("***********主线程开始***********")
import threading
import time


def f1():
    print("***********f1开始***********")
    # time.sleep(s)
    print("***********f1结束***********")

def f2():
    print("***********f2开始***********")
    # time.sleep(s)
    print("***********f2结束***********")

def f3():
    for i in range(100):
        f1()

def f4():
    for i in range(100):
        f2()
# 创建线程
# target 指定这个线程执行哪个函数中的代理，只写函数名即可，不要写括号
# args 后面指定的是一个元组
th1 = threading.Thread(target=f3)
th2 = threading.Thread(target=f4)
# th1 = threading.Thread(target=f1, args=(1,))
# th2 = threading.Thread(target=f2, args=(1,))

# 启动线程
th1.start()
th2.start()

# 设置线程等待 .join()
th1.join()
th2.join()

print("***********主线程结束***********")





