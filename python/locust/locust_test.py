# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-06 18:54   #2025/6/6 18:54
@File：locust05.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
常用的脚本增强技术：
- 关联：解决请求之间的依赖关系
    将脚本中的某些写死的数据，变成来自服务器的动态的每次不一样的数据
    先存：通过一定的手段将服务器返回的数据进行捕获并且保存
    后用：在需要关联的地方，调用保存的数据
    正则表达式/jsonpath/lxml
- 参数化：实现逻辑相同，数据不同的场景
    队列：queue
        queue.qsize：返回当前队列包含的消息数量
        queue.empty：如果队列为空，返回true
        queue.full：如果队列满了，返回true
        queue.put_nowait(item)相当于queue.put(item,False)

- 断言（检查点）
- 思考时间
- 事务（task）
- 集合点
"""
import re
import os
import requests,csv

# 使用正则处理

token = ""

def a():
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
    res = requests.post(url, data=data, headers=headers)
    print(res.text)
    p = r'"access_token":"(.*?)",'
    com = re.compile(p)
    token = re.findall(com, res.text)
    print(token)

# a()
def querypage(self):
    url = "http://saastestadminboss2023.adre45.com/api/mgt/report/bigdata-player-manage/base-info-page"
    headers = {
        "authorization": "Basic c2FhczpzYWFzX3NlY3JldA==",
        "content-type": "multipart/form-data",
        "host": "saastestadminboss2023.adre45.com",
        "origin": "http://saastestadminboss2023.adre45.com",
        "referer": "http://saastestadminboss2023.adre45.com/",
        "identity-type": "user",
        "saas-auth": f"bearer {token}"
    }
    data = {"tenantIds": ["1007"], "query": {"sorts": [{"field": "", "isAsc": ""}], "current": 1, "size": 10}}
    res = self.client.post(url, json=data, headers=headers)
    assert res.status_code == 200


userids = []
with open("data_csv/data.csv", "r") as f:
    data = csv.reader(f)
    for row in data:
        # print(row) ['1', '5436057']
        userids.append(row[1])

print(userids)

