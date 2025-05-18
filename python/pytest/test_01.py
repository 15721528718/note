# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-05 15:00   #2025/5/5 15:00
@File：pytest01.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import pytest
import csv
"""
为add函数写测试用例
"""
def add(a: object, b: object) -> object:
    return a+b

def read_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        return list(data)


class TestAdd(object):

    @pytest.mark.api 
    def test_int(self):
        res = add(1,2)
        assert res == 3
    @pytest.mark.web
    def test_str(self):
        res = add('hello','world')
        assert res == 'helloworld'
    @pytest.mark.ut
    def test_list(self):
        res = add([1,2,3],[4,5,6])
        assert res == [1,2,3,4,5,6]
    @pytest.mark.login
    @pytest.mark.usefixtures
    def test_dict(self):
        res = add({'a':1,'b':2},{'c':3,'d':4})
        assert res == {'a':1,'b':2,'c':3,'d':4}

    @pytest.mark.canshu
    @pytest.mark.parametrize(
        'a,b,c',
        read_csv("data.csv")
    )
    def test_param(self,a,b,c):
        res = add(int(a),int(b))
        assert res == int(c)

