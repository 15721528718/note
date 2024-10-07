# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-06 17:43   #2024/10/6 17:43
@File：面向对象-特点-继承.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
super().__ init__ ()有什么用？
1.super().__init__() 、 super(B,self).__init__()
super()用来调用父类(基类)的方法，__init__()是类的构造方法，
super().__init__() 就是调用父类的init方法， 同样可以使用super()去调用父类的其他方法。

2、super(). __ init __()
如果子类B和父类A，都写了init方法，
那么A的init方法就会被B覆盖。想调用A的init方法需要用super去调用。
(1).B覆盖了父类A的init：
class A:
    def __init__(self):
        print('A的init被调用了')
class B(A):
    def __init__(self):
        print('B的init被调用了')
b = B()
# B的init被调用了

(2).B覆盖了父类A的init,通过super又调用了A的init：
class A:
    def __init__(self):
        print('A的init被调用了')
class B(A):
    def __init__(self):
        super().__init__()
        print('B的init被调用了')
b = B()
# A的init被调用了
# B的init被调用了


当然，在B内部，除了用super调用父类的方法，也可以用父类名调用，例：
class B(A):
    def __init__(self):
        A.__init__(self)
        print("B init")

3.关于覆盖
有人可能会误解“覆盖”的意思，认为“覆盖”了就是没有，为什么还能通过super调用？
覆盖了并不是没有了，A的方法终都还在，但需要在B内部用super调用。

例：
A里写了一个方法hi(), B继承自A, B里也写了一个方法hi()。
B的对象在外部调用hi(), 就只能调用B里面写的这个hi()。
想通过B调用A的hi(),只能在B内部用super().hi()调用。

class A:
    def hi(self):
        print("A hi")

class B(A):
    def hello(self):
        print("B hello")
        
b = B()
b.hi()       # B里没有写hi(),这里调用的是继承自A的hi()

------------------------------------------------------------------
class A:
    def hi(self):
        print("A hi")

class B(A):
    def hi(self):
        print("B hi")
        
b = B()
b.hi()    # 这里调用的就是B自己的hi()
------------------------------------------------------------------
class A:
    def hi(self):
        print("A hi")

class B(A):
    def hi(self):
        super().hi()         # 通过super调用父类A的hi()
        print("B hi")
        
b = B()
b.hi()    # 这里调用的就是B里面的hi()

"""