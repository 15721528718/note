# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-08 18:59   #2025/6/8 18:59
@File：locust07.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
注意：框架本身没有直接封装集合点的概念 ，间接通过gevent并发机制，使用gevent的锁来实现
semaphore是一个内置的计数器： 每当调用acquire()时，内置计数器-1 每当调用release()时，内置计数器+1 计数器不能小于0，当计数器为0时，acquire()将阻塞线程直到其他线程调用release()
两步骤：
    1.all_locusts_spawned 创建钩子函数
    2.将locust实例挂载到监听器 events.spawning_complete.add_listener
    3.Locust实例准备完成时触发
   

"""

# 集合点
from locust import HttpUser, TaskSet, task, events, between
# from gevent._semaphore import Semaphore
from gevent.lock import Semaphore
import os,re

all_locust_spawned = Semaphore()
all_locust_spawned.acquire() # 阻塞

# 添加集合点事件处理器
@events.spawning_complete.add_listener    # 所有的locust实例产生完成时触发
def on_spawning_complete(**kwargs):
    all_locust_spawned.release() # 创建钩子方法


n=0
class UserBehaviour(TaskSet):
    def login(self):
        global n
        n += 1

        url = "/api/mgt/auth/oauth/token?grant_type=password&scope=all&username=Bee99&password=1d3b393b812ac1b2661fbc2cbfbf8366&pageType=2&pwdLevel=2"
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
        res = self.client.post(url, data=data, headers=headers)
        p = r'"access_token":"(.*?)",'
        com = re.compile(p)
        self.token = re.findall(com, res.text)


        print("%s 个虚拟用户开始启动，并登录" %n)

    def loginput(self):
        print("退出登录")

    def on_start(self):
        self.login()
        all_locust_spawned.wait()  # 同步锁等待时间

    @task(1)
    def querypage(self):
        url = "/api/mgt/report/bigdata-player-manage/base-info-page"
        headers = {
            "authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
            "content-type": "multipart/form-data",
            "host": "saastestadminboss2023.adre45.com",
            "origin": "http://saastestadminboss2023.adre45.com",
            "referer": "http://saastestadminboss2023.adre45.com/",
            "identity-type": "user",
            "saas-auth": f"bearer {self.token}"
        }
        data = {"tenantIds": ["1007"], "query": {"sorts": [{"field": "", "isAsc": ""}], "current": 1, "size": 10}}
        with self.client.post(url, json=data, headers=headers, catch_response=True) as r:
            if r.status_code == 200:
                r.success()
            else:
                r.failure("Failed to query page")




class WebsiteUser(HttpUser):
    task_set = task(UserBehaviour)
    host = "http://saastestadminboss2023.adre45.com"
    wait_time = between(1, 2)

if __name__ == '__main__':
    os.system("locust -f locust07.py")