# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-03 18:36   #2024/10/3 18:36
@File：文件.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import os

path = os.getcwd()
filename = path + '/test.txt'
# 打开文件
f=open(filename,mode='a+',encoding='utf-8')
"""
r 只读【默认模式，文件必须存在，不存在则抛出异常】
w 只写，写之前会清空文件的内容，如果文件不存在，会创建新文件
a 追加的方式，在原本内容中继续写，如果文件不存在，则会创建新文件
r+ 可读可写
w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果文件不存在，创建新文件用于读写。
b rb、wb、ab、rb+、wb+、ab+意义和上面一样，用于二进制文件操作
"""
# 读取文件
# context = f.read() #读取文件全部内容
# print(context)
# context1 = f.readline() #读取文件的第一行
# print(context1)
# context2 = f.readlines() #按行读取文件全部内容，把每一行放到一个列表中
# print(context2)

# 写入文件
f.write('你你你你你你你\n')
f.writelines('我我我我我我我\n')

# 关闭文件
f.close()

# with语句
with open('test.txt','r',encoding='utf-8') as f:
    context3 = f.read()
    print(context3)