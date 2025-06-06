# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-06 15:28   #2025/6/6 15:28
@File：locust04.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from locust import HttpUser,task,TaskSet

class DemoTaskSet(TaskSet):
    def test_case1(self):
        self.client.get("/")

    def test_case2(self):
        self.client.post("/")



