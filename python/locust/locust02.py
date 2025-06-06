# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-06 02:28   #2025/6/6 02:28
@File：locust02.PY
@IDE：PyCharm
@Motto：南风知我意
"""

# locust脚本模版

from locust import HttpUser, task, between, TaskSet


class UserBehavior(TaskSet):

    # 启动locust时 setup
    def setup(self):
        print("task setup")

    # 停止locust时 teardown
    def teardown(self):
        print("task teardown")

    # 虚拟用户启动task时运行
    def on_start(self):
        print("start")

    # 虚拟用户结束task时运行
    def on_stop(self):
        print("stop")

    @task(1)
    def index(self):
        self.client.get("/")
        print("index")
        assert 1==1

    @task(2)
    def info(self):
        self.client.get("/info")
        print("info")
        assert 1==2

class WebsiteUser(HttpUser):

    def setup(self):
        print("locust setup")

    def teardown(self):
        print("locust teardown")


    host = "http://127.0.0.1:8000"
    task_set = task(UserBehavior)
    # tasks = [UserBehavior]
    # wait_time = between(3, 5)
    min_wait = 3000 # 单位是毫秒，最小等待时间
    max_wait = 5000 # 单位是毫秒，最大等待时间

