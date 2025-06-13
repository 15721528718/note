# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-12 11:04   #2025/6/12 11:04
@File：logging01.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import logging
import requests,re
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s:%(lineno)ds - %(levelname)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S',filename='logging.log',filemode='w')

# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')


def login():
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
    p = r'"access_token":"(.*?)",'
    com = re.compile(p)
    token = re.findall(com, res.text)
    # print(token)
    logging.info(token)
    return token

def querypage():
    token = login()
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
    res = requests.post(url, json=data, headers=headers)
    logging.info(res.text)


querypage()