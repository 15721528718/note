# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-06 14:46   #2025/6/6 14:46
@File：locust03.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from locust import HttpUser,task,TaskSet

class ScriptTasks(TaskSet):
    # 初始化，每个虚拟用户开始做的第一件事情
    def on_start(self):
        pass

    # @task(2)装饰器方法为一个事务，方法的参数指定该行为的执行权重，参数越大，每次被虚拟用户执行的概率越高，默认为1.
    # 创建一个访问首页的方法
    @task(2)
    def index(self):
        # self.client 使用python requests库的方法，调用和使用方法跟requests一样
        self.client.get("http://saastestadminboss2023.adre45.com/#/login")

    # 创建一个登录的方法
    @task(1)
    def login(self):
        url = "http://saastestadminboss2023.adre45.com/api/mgt/auth/oauth/token?grant_type=password&scope=all&username=Bee99&password=1d3b393b812ac1b2661fbc2cbfbf8366&pageType=2&pwdLevel=2"
        data = {
            "grant_type": "password",
            "pageType": 2,
            "password": "1d3b393b812ac1b2661fbc2cbfbf8366",
            "pwdLevel": 2,
            "scope": "all",
            "username": "Bee99"
        }
        headers = {
            "authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
            "content-type": "multipart/form-data",
            "host": "saastestadminboss2023.adre45.com",
            "origin": "http://saastestadminboss2023.adre45.com",
            "referer": "http://saastestadminboss2023.adre45.com/",
            "identity-type": "user"
        }
        self.client.post(url, data=data, headers=headers)

class WebsiteUser(HttpUser):

    # 指向一个定义好的用户行为
    task_set = task(ScriptTasks)
    # 被测系统的host
    host = "http://saastestadminboss2023.adre45.com"
    # 每个用户执行两个任务的间隔时间
    min_wait = 1000 # 单位是毫秒，最小等待时间
    max_wait = 3000 # 单位是毫秒，最大等待时间

# TaskSet用法
"""
TaskSet实现了虚拟用户所执行任务的调度方法，包括：
- 任务执行顺序：schedule_task
- 指定下一个执行的任务：execute_next_task
- 执行任务：execute_task
- 休眠等待：wait_task  # loadruuner: 思考时间 pacing（步长）：迭代之间的等待
- 中断：interrupt_task
"""











