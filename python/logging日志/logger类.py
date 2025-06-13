# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-06-12 13:14   #2025/6/12 13:14
@File：logger类.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import logging

log1 = logging.Logger("hello")
log2 = logging.Logger("hello")
print(log1, log2, type(log1), type(log2), id(log1), id(log2),log1 is log2)

log3 = logging.getLogger("hello") # 工厂模式
log4 = logging.getLogger("hello") # 同样的名称，返回同样的实例；不同的名称字符串对应不同的实例

# 根logger
root1 = logging.root
root2 = logging.Logger.root
root3 = logging.getLogger()

print(log3, log4, type(log3), type(log4), id(log3), id(log4),log3 is log4)




