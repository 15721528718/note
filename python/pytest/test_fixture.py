# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-08 16:43   #2025/5/8 16:43
@File：test_fixture.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import pytest

@pytest.fixture
def f():
    print("前置操作")
    # 前置操作
    yield
    # 后置操作
    print("后置操作")

"""
使用fixfure
    1.再用例的参数列表中，加入fixture名字即可
    2.给用例加上usefixtures标记
"""
def test_1(f):
    print("用例test_1开始执行")
    assert 1==1
    print("用例test_1执行结束")

@pytest.mark.usefixtures("f")
def test_2():
    print("用例test_2开始执行")
    assert 2==2
    print("用例test_2执行结束")