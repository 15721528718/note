# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-05-06 18:05   #2025/5/6 18:05
@File：pytest01.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import csv
import yaml
import json

def read_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        return list(data)
# a = read_csv("data.csv")
# print(a)

with open('aaa.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    json_data = json.dumps(data, indent=4)
    print(json_data)