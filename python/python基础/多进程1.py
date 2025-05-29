# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-29 16:57   #2025/5/29 16:57
@File：多进程1.PY
@IDE：PyCharm
@Motto：南风知我意
"""
# 导入进程包
import multiprocessing
import time
"""
Process类的说明
    Process([group[,target[,name[,[,args[,kwargs]]]]]])
     group：指定进程组，目前只能使用None
     target：执行的目标任务名
     name：进程名字
     args：以元组方式给执行任务传參
     kwargs：以字典方式给执行任务传參
     
    Process创建的实例对象的常用方法：
     start()：启动子进程实例（创建子进程）
     join()：等待子进程执行结束
     terminate()：不管任务是否完成，立即终止子进程
     
    Process创建的实例对象的常用属性：
     name：当前进程的别名，默认为Process-N , N为从1开始递增的整数
"""

def f1():
    print("任务一开始")
    time.sleep(2)
    print("任务一结束")

def f2():
    print("任务二开始")
    time.sleep(3)
    print("任务二结束")

pr1 = multiprocessing.Process(target=f1)
pr2 = multiprocessing.Process(target=f2)

pr1.start()
pr2.start()

