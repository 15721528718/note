# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-22 21:08    #2025/5/22 21:08
@File：locust01.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
locust框架的组成和工作流程

"""
from locust import HttpUser, TaskSet


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
    tasks = [UserCollects]
