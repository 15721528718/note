# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-10 13:03   #2024/10/10 13:03
@File：环境及平台.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from Encapsulation.VAR.VAR import *
import requests
import logging

class GetParams:
    def __init__(self,environment, backstage):
        """

        :param environment: 环境（testev，uatev）
        :param backstage: 后台（shanghu，yunying）
        :return:
        """
        self.url = ''
        self.data = ''
        self.headers = ''
        self.environment = environment
        self.backstage = backstage
    @property
    def gettoken(self):
        self.url = LOGINPARAMS[self.environment][self.backstage]['url']
        self.headers = LOGINPARAMS[self.environment][self.backstage]['headers']
        self.data = LOGINPARAMS[self.environment][self.backstage]['data']
        res = requests.post(self.url, headers=self.headers, data=self.data)
        access_token = res.json()['access_token']
        return access_token
    @property
    def get_url_headers(self):
        access_token = self.gettoken
        originurl = LOGINPARAMS[self.environment][self.backstage]['headers']['origin']
        headers = LOGINPARAMS[self.environment][self.backstage]['headers']
        headers['content-type'] = 'application/json;charset=UTF-8'
        headers['saas-auth'] = ' '.join(['bearer ', access_token])
        return originurl, headers

class TestLog:
    def __init__(self):
        pass

    """
    level 表示设置的日志等级
    format 表示日志的输出格式, 参数说明:
    %s:格式化输出文字或数字
    %d:格式化输出数字
    %(levelname)s: 打印日志级别名称
    %(filename)s: 打印当前执行程序名
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(message)s: 打印日志信息
    """
    def test_log(self):
        # 创建日志器
        logger = logging.getLogger()
        # 设置日志级别
        logger.setLevel(logging.DEBUG)
        #  防止重复写日志，这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not logger.handlers:
            # 指定日志信息显示在哪里 哪个组件 控制台 文本文件 处理器
            # 创建处理器 控制台处理器
            ch = logging.StreamHandler()
            # 把日志信息添加到控制台
            logger.addHandler(ch)

            # 把日志信息显示到文本文件
            # 创建文本处理器 文件放到哪里 文件地址
            fh = logging.FileHandler('test.log',mode='a',encoding='utf-8')
            # 日志信息显示到文本文件中
            logger.addHandler(fh)

            # 格式器 设置自定义格式
            fmt = '%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] - %(message)s'
            formatter = logging.Formatter(fmt)

            # 给控制台设置格式
            ch.setFormatter(formatter)
            # 给日志文件设置格式
            fh.setFormatter(formatter)

        return logger
    def loglog(self):
        logger = logging.getLogger()
# 把日志信息保存在日志器中
testlog = TestLog()
if __name__ == '__main__':
    testlog.test_log().debug('debug级别的日志')