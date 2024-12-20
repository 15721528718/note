# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-09-28 09:18   #28/9/2024 AM9:18
@File：元组与集合.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
元组：不可变序列，不能进行增删改操作

元组的创建方式：
1.直接小括号
t = ('python','hello',90)
2.使用内置函数tuple()
t = tuple(('haha','hello',90))
3.只包含一个元素的元组需要使用逗号和小括号
t = (10 , )

集合：可变序列，是没有value的字典
集合的创建：
1.使用{}
s = {1,2,3,4,5,6}  集合中的元素不允许重复
2.使用内置函数set()
s = set()

集合的相关操作：
1.集合元素的判断操作
in或not in
2.集合元素的新增操作
调用add()方法   一次添加一个元素    s.add(80)
调用update()方法   一次至少添加一个元素    s.update({200,300,400})/s.update([500,600,700])/s.update((201,301,401))
3.集合元素的删除操作
调用remove()方法   一次删除一个指定元素，如果指定的元素不存在，抛出KeyError     s.remove(200)
调用discard()方法   一次删除一个指定元素，如果指定的元素不存在，不抛异常     s.discard(300)
调用pop()方法   一次删除一个任意元素    s.pop()  不能加参数
调用clear()方法   清空集合

集合间的关系：
1.两个集合是否相等（元素相同，就相等）
s1 == s2    s1 != s2
2.一个集合是否是另一个集合的子集
s1={1,2,3,4,5,6}
s2={1,2,3}
s3={1,2,9}
s2.issubset(s1)  True
s3.issubset(s1)  False
3.一个集合是否是另一个集合的超集
s1.issuperset(s2)  True
s1.issuperset(s3)  False
4.两个集合是否含有交集
s2.isdisjoint(s3)   False  有交集为false，没有交集为true

集合的数据操作：
s1={1,2,3,4,5,6}
s2={1,2,3,7}
s3={1,2,9}
1.交集
s1.intersection(s2)
s1 & s2                        intersection()与&等价，交集操作
2.并集
s1.union(s2)
s1 | s2                         union()与|等价，并集操作
3.差集
s1.difference(s2)
s1-s2
4.对称差集
s1.symmetric_difference(s2)

集合生成式：
{i*i for i in range(10)}
"""
