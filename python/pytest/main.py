# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-05 15:03   #2025/5/5 15:03
@File：main.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import pytest
import os
if __name__ == '__main__':
    pytest.main(['-vv','-s', '../pytest/test_fixture.py'])  #,'-m canshu'
    os.system("allure generate ./temps -c -o ./report")
"""
pytest常用第三方插件
1.pytest-html
    安装：pip install pytest-html
    使用：--html=report.html --self-contained-html
    
2.pytest-xdist    用途：分布式执行
    安装：pip install pytest-xdist
    使用：-n 进程数量
    只有在任务本身耗时较长，超出调用成本很多的时候，才有意义
    分布式执行，有并发问题：资源竞争、乱序

3.pytest-rerunfailures    用途：用例失败后，重新执行
    安装：pip install pytest-rerunfailures
    使用：--reruns 次数 --reruns-delay 时间
    
4.pytest-result-log    用途：把用例的执行结果记录到日志文件中
    安装：pip install pytest-result-log
    使用：在配置文件中（pytest.ini）
"""
"""
allure
安装：pip install allure-pytest
配置：--alluredir=temps --clean-alluredir
生成报告：allure generate -o report -c temps
"""