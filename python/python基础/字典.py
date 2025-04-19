# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-09-28 09:17   #28/9/2024 AM9:17
@File：字典.PY
@IDE：PyCharm
@Motto：南风知我意
"""
# 1.字典的创建
# a = {"asd": 2,"sdf":56}
# b = dict(asd=2,sdf=56)
#
# 2.字典的常用操作
# []和get()方法---scores.get('asd')
# 区别：
# 	[]如果字典中不存在指定的key，抛出keyError异常
# 	get()方法取值。如果字典中不存在指定的key，并不会抛出异常，而是会返回None，可以通过参数设置默认的value，以便指定的key不存在时返回。
#
# key的判断：in   not in
#
# 字典元素的删除： del scores['张三']
#
# 字典元素的新增： scores['asdfg'] = 90
#
# 字典元素的修改： scores['asdfg'] = 900
#
# 获取字典视图的三个方法：
# 	keys() ：获取所有的键
# 	values() ：获取所有的值
# 	items() ：获取字典中所有键值对
#
#
# 字典的特点：
# 1.key不允许重复，value可以重复
# 2.字典中的元素是无序的
# 3.字典中的key必须是不可变对象
# 4.字典也可以根据需要动态地伸缩
# 5.字典会浪费较大的内存，是一种用空间换时间的数据结构
#
#
# 字典生成式：
# items = ['fruits','books','others']
# prices = [50,60,70]
#
# { item:price for item,price in zip(items,prices)}