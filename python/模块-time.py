# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-02 13:16   #2024/10/2 13:16
@File：模块-re模块-正则表达式.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import re,time
a = time.time() #时间戳：1970年
print(a)
t = time.localtime() #结构化的时间
print(t)
print(t.tm_year)
s = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(s)

