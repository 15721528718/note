# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-22 21:08    #2025/5/22 21:08
@File：locust01.PY
@IDE：PyCharm
@Motto：南风知我意
"""

from locust import HttpUser, TaskSet,between,task


# def requestCode(self):
#     self.client.get("/")
# def mlogin(self):
#     self.client.get("/login")

# 定义我们的任务集
class UserCollects(TaskSet):

    # 开始的时候会调用on_start 只调用一次
    def on_start(self):
        print("调用了on_start方法")

    # 结束的时候会调用on_stop 只调用一次
    def on_stop(self):
        print("调用了on_start方法")


class UserBehavior(HttpUser):
    # tasks = [UserCollects]

    # 设置一个随机事时间间隔
    wait_time = between(3, 5)

    def on_start(self):
        print("HttpUserBehavior on_start")

    @task(1)
    def index(self):
        self.client.get("/index")
        print("执行了index方法")
    @task(4)
    def about(self):
        self.client.post("/about")
        print("执行了about方法")

    def on_stop(self):
        print("HttpUserBehavior on_stop")
"""
有关locust关键类的说明

client：requests封装后的
self.client = HttpSession(base_url=self.host) ==>继承requests.Session

tast_set：用于定义用户的任务信息
max_wait/min_wait
host
weight：用于控制任务执行的权重
"""