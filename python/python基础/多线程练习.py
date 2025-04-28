# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-27 09:14   #2025/4/27 09:14
@File：多线程练习.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from threading import Thread,Lock
import time
print("主线程开始")

app_lock = Lock()

def f1():
    print("f1开始上锁")
    app_lock.acquire()
    print("f1上锁成功")
    print("******************")
    time.sleep(5)
    print("f1开始解锁")
    app_lock.release()
    print("f1解锁成功")

def f2():

    app_lock.acquire()
    print("f2开始上锁")
    print("f2上锁成功")
    print("******************")
    time.sleep(2)
    print("f2开始解锁")
    app_lock.release()
    print("f2解锁成功")

th1 = Thread(target=f1)
th2 = Thread(target=f2)

th1.start()
th2.start()

th1.join()
th2.join()

print("主线程结束")