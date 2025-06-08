# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-08 16:21   #2025/6/8 16:21
@File：locust06.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
- 参数化：实现逻辑相同，数据不同的场景
    队列：queue
        queue.qsize：返回当前队列包含的消息数量
        queue.empty：如果队列为空，返回true
        queue.full：如果队列满了，返回true
        queue.put_nowait(item)相当于queue.put(item,False)
"""
from locust import HttpUser,TaskSet,task
import re,os
import csv
# 场景一：循环取值，可以重复使用数据
class UserBehavior(TaskSet):
    def on_start(self):
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
        self.token = re.findall(com, res.text)[0]
        # print(self.token)

        self.index = 0

    @task(1)
    def task_query(self):
        url = "/api/mgt/report/bigdata-player-manage/base-info-page"
        headers = {
            "authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
            "content-type": "application/json",
            "host": "saastestadminboss2023.adre45.com",
            "origin": "http://saastestadminboss2023.adre45.com",
            "referer": "http://saastestadminboss2023.adre45.com/",
            "identity-type": "user",
            "saas-auth": f"bearer {self.token}"
        }

        data = {"tenantIds":["1007"],"playerId":self.parent.userids[self.index],"query":{"sorts":[{"field":"","isAsc":""}],"current":1,"size":10}}
        with self.client.post(url, json=data, headers=headers,catch_response=True) as res:

            if res.json()["data"]["records"][0]["id"] == self.parent.userids[self.index]:
                res.success()
            else:
                res.failure("失败了")

        self.index = (self.index + 1) % len(self.parent.userids)

class WebsiteUser(HttpUser):
    task_set = task(UserBehavior)
    host = "http://saastestadminboss2023.adre45.com"
    min_wait = 3000
    max_wait = 5000

    userids = []
    with open("data_csv/data.csv", "r") as f:
        data = csv.reader(f)
        for row in data:
            # print(row) ['1', '5436057']
            userids.append(row[1])

if __name__ == "__main__":
    os.system("locust -f locust06.py")