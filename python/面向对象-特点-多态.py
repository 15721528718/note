# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-07 10:14   #2024/10/7 10:14
@File：面向对象-特点-多态.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
1、什么是多态
多态是指对象通过他们共同的属性和方法来操作及访问，而不需要考虑他们具体的类。
"""
s = "abc"
print(s.__len__())  # 3，等同len(s)

l = [1, 3]
print(l.__len__())  # 2,等同len(l)
"""多态体现在由同一个类实例化出多个对象，这些对象执行相同的方法时，执行的过程和结果是不一样的。"""
class H2O:
    def __init__(self, name, tem):
        self.name = name
        self.tem = tem

    def turn(self):
        if self.tem > 100:
            print("%s 变成了水蒸气" % self.name)
        elif self.tem < 0:
            print("%s 变成了冰" % self.name)
        else:
            print("%s 变成了水" % self.name)

class Steam(H2O):
    pass
class Water(H2O):
    pass
class Ice(H2O):
    pass

s = Steam("s", 1000)
w = Water("w", 50)
i = Ice("i", -10)

s.turn()    # s 变成了水蒸气
w.turn()    # w 变成了水
i.turn()    # i 变成了冰

"""
2、多态小实验
模拟 len() 函数，对上述turn方法，做成函数形式。
"""
# 接上述实例化代码后，补充如下代码
def turn(obj):
    obj.turn()

turn(s) # s 变成了水蒸气
turn(w) # w 变成了水
turn(i) # i 变成了冰
