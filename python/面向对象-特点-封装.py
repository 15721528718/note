# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-07 10:14   #2024/10/7 10:14
@File：面向对象-特点-多态.PY
@IDE：PyCharm
@Motto：南风知我意
"""
"""
1、什么是封装
（1）装，即把一些属性装到一个容器中。封，即为隐藏。
（2）类就是一种容器，这本身就是一种封装。
（3）类中定义私有的属性，只有类的内部可以使用，外部无法访问。
（4）封装明确区分内外，内部的实现逻辑，外部无法知晓，并且为封装到内部的逻辑提供一个访问接口给外部使用。
2、内部属性的约定
python并没有严格限制外部访问内部属性，但把单下划线和双下划线开头的属性约定为内部属性。
"""
class People:
    _age = 18
    __sex = "f"
    def __init__(self):
        pass

    def info(self):
        print("age %s,sex %s" %(self._age, self.__sex))
        # 在类的方法内部会自动将 __sex 转换为 _People__sex
p1 = People()
print(People._age)  # 18 单下划线开头属性，外部可以直接访问
print(People._People__sex)  # f 双下划线开头属性，会在属性字典中重命名为_类__属性
p1.info()   # age 18,sex f 内部可以调用它们
"""
1.1 如何实现封装？
封装可以通过访问控制和访问修饰符来实现。主要有两种访问修饰符：公有属性和方法、私有属性和方法。
公有属性和方法 (Public Attributes and Methods)
可以被类的外部访问。在 Python 中，默认情况下，类的所有属性和方法都是公有的。
"""
class Person:
    def __init__(self, name, age):
        self.name = name  # 公有属性
        self.age = age  # 公有属性

    def get_name(self):
        return self.name  # 公有方法

# 使用公有属性和方法
person1 = Person("Tiyong", 30)
print(person1.name)  # 输出: Tiyong
print(person1.get_name())  # 输出: Tiyong
"""
在这个例子中，Person类有一个公有方法 get_name()，那么其他类或代码可以通过调用这个方法来获取对象的名称。同样，有一个公有属性 age，那么其他类或代码可以直接访问和修改这个属性。所以，我们的实例对象就可以访问公共的属性和方法。

私有属性和方法 (Private Attributes and Methods)
只能在类的内部访问，外部无法直接访问。在 Python 中，可以在属性名或方法名前加上双下划线 ‘__’ 来定义私有属性和方法。
"""
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age  # 私有属性

    def __display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"  # 私有方法

# 外部无法直接访问私有属性和方法
person1 = Person("TiYong", 25)
# print(person1.__name)  # 这会引发错误，因为__name是私有属性
# print(person1.__display_info())  # 这会引发错误，因为__display_info()是私有方法
"""
在上面的例子中：person1对象就不能访问__name私有属性和__display_info()私有方法。
尽管外部无法直接访问私有属性和方法，但我们仍然可以通过公有方法来间接访问和操作它们。这种间接访问的方式使得我们可以
控制对象的状态和行为，确保数据的一致性和安全性。
"""
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age  # 私有属性

    def get_name(self):
        return self.__name  # 公有方法

    def set_name(self, new_name):
        self.__name = new_name  # 公有方法，用于修改私有属性

    def display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"  # 公有方法

# 通过公有方法访问和修改私有属性
person1 = Person("TiYong", 30)
print(person1.get_name())  # 输出: TiYong
person1.set_name("Toy")
print(person1.display_info())  # 输出: Name: Toy, Age: 30

