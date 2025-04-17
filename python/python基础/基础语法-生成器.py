# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-13 18:00   #2024/10/13 18:00
@File：基础语法-装饰器.PY
@IDE：PyCharm
@Motto：南风知我意
"""
# 方式一 创建生成器和通过列表推导式创建列表类似，只需将[]换为()
print("********方式一********")
# 列表推导式
list1 = [i for i in range(10)]
print(list1)

# 创建生成器
g = (i for i in range(10))
# 打印类型为<class 'generator'>
print(type(g))
# 注意，生成器直接输出，只能打印出在内存中的地址 <generator object <genexpr> at 0x105908340>
print(g)

# 输出生成器的结果有两种方式
#g.__next__()    next(g)
g = (i for i in range(2))
# 输出每次结果
print(g.__next__())
print(g.__next__())

a = (i for i in range(2))
print(next(a))
print(next(a))


# 方式二
print("********方式二********")
def fun():
    n = 0
    while True:
        n += 1
        # 注意，yield的作用是return + 停止
        yield n
b = fun()
# 注意，输出同样可以使用next()或者__next__()方式
print(next(b))
print(b.__next__())

# 终止生成器
# 生成器可以通过StopIteration异常来正常结束，或者通过外部代码调用close()
# 方法来强制结束。

def gen():
    yield 1
    yield 2


gen_obj = gen()
next(gen_obj)  # 输出1
gen_obj.close()  # 终止生成器
