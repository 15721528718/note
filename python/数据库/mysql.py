# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-25 13:23   #2025/4/25 13:23
@File：mysql.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import pymysql

# 1.连接mysql
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="mysql123456",charset="utf8mb4",db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送指令---插入数据
# cursor.execute("insert into admin (username,password,mobile) values ('sadsdsa','a1234567','15723457268')")
# 方式一：传列表或元组
# sql = "insert into admin (username,password,mobile) values (%s,%s,%s)"
# cursor.execute(sql,('admin','123456','19999999999')) #可以传列表或元组

# 方式二：传字典
# sql = "insert into admin (username,password,mobile) values (%(name)s,%(pwd)s,%(mob)s)"
# cursor.execute(sql,{"name":"小明","pwd":"sa1243432","mob":"15712342456"})
#
# conn.commit()


# 2.发送指令---查询并获取数据
cursor.execute('select * from admin limit 1')
datalist = cursor.fetchall() # 获取查询到的所有数据，返回的是一个列表，列表中每个字典代表一行数据。
# dataone = cursor.fetchone() # 获取查询到的数据的第一条数据,返回的是一个字典。
print(datalist)
# print(dataone)


# 2.发送指令---删除数据

# 2.发送指令---修改数据

# 3.关闭
cursor.close()
conn.close()