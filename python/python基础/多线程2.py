# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-15 16:13   #2025/4/15 16:13
@File：多线程.PY
@IDE：PyCharm
@Motto：南风知我意
"""

print("***********主线程开始***********")
from threading import Thread,Lock
from time import sleep

# 存储支付宝账号和余额
zhifubao = {
    "zhangsan": 10000,
    "liming": 5000,
    "wanghong": 3000,
    "zhaolei": 5000,
}

# 申请一把锁
zhifu_lock = Lock()

# 线程1: 嘀嘀打车处理，参数是用户账户和扣款金额
def thread1_didi_pay(account, amount):
    print("* t1：即将开始操作")

    # 上锁
    zhifu_lock.acquire()

    balance = zhifubao[account]

    # 下面的sleep（2）表示一些处理过程需要花上2秒
    print("* t1：完成交易需要2s钟")
    sleep(2)

    print("* t1：deduct")
    zhifubao[account] = balance - amount

    #释放锁
    zhifu_lock.release()

    # 输出交易后的余额
    print(f'{account}的余额为', zhifubao[account])

# 线程2: 余额宝可以赚取利息，参数是用户账户和扣款金额
def thread2_yue_pay(account, amount):
    print("* t2：即将开始操作")

    # 上锁
    zhifu_lock.acquire()

    balance = zhifubao[account]

    # 下面的sleep（2）表示一些处理过程需要花上2秒
    print("* t2：完成交易需要2s钟")
    sleep(2)

    print("* t2：deduct")
    zhifubao[account] = balance + amount

    # 释放锁
    zhifu_lock.release()

    # 输出交易后的余额
    print(f'{account}的余额为', zhifubao[account])

# 分别创建两个线程
t1 = Thread(target=thread1_didi_pay, args=("liming", 2000))
t2 = Thread(target=thread2_yue_pay, args=("liming", 3000))

# 启动线程
t1.start()
t2.start()

# 设置线程等待
t1.join()
t2.join()

print("***********主线程结束***********")


