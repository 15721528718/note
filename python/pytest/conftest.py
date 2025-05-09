# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-09 11:42   #2025/5/9 11:42
@File：conftest.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import pytest
@pytest.fixture(scope="session")
def ff():
    print("我是第二个fixture，但是被fixture使用")   #依赖使用


@pytest.fixture(autouse=True,scope='session')
def f(ff):
    print("前置操作")
    # 前置操作
    yield
    # 后置操作
    print("后置操作")
"""
autouse  每个用例都自动使用
scope   作用范围：function：默认值，对每个测试方法（函数）生效，生命周期在测试方法级别
                class：对测试类生效，生命周期在测试类级别
                module：对测试模块生效，生命周期在模块（文件）级别
                package：对测试包生效，生命周期在测试包（目录）级别
                session：全局。对测试会话生效，生命周期在会话（一次pytest运行）级别。使用conftest.py
"""
"""
使用fixfure
    1.再用例的参数列表中，加入fixture名字即可
    2.给用例加上usefixtures标记
"""