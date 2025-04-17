# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-03 18:36   #2024/10/3 18:36
@File：文件.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import csv
import os

path = os.getcwd()
csvname = path + '/data.csv'

with open(csvname, 'r', encoding='utf-8') as f:
    cf = csv.reader(f)
    head = next(cf)
    for i in cf:
        print(i)

with open(csvname, 'a', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([8,'h','八'])
    writer.writerows([[7,'g','七'],[7,'g','七'],[7,'g','七'],[7,'g','七'],[7,'g','七']])
