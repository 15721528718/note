# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-09-29 11:03   #29/9/2024 AM11:03
@File：bug及异常.PY
@IDE：PyCharm
@Motto：南风知我意
"""

"""
bug的常见类型
    1.粗心导致的语法错误 SyntaxError
    2.知识点不熟悉导致的错误
        1.索引越界问题IndexError
        2.append()方法的使用不熟练
    3.思路不清导致的问题
    4.被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些“例外情况”而导致的程序崩溃
        解决方案：异常机制
        try:
        except BaseException as e:
        else:
        finally:
        
        raise关键字：
        原：
            pwd=input('请输入你的密码：')
            if len(pwd)<8:
                print('密码的长度不够，请输入一个8位以上的密码')
            else:
                print('登录操作')
                
        使用raise关键字后：
            try:
                pwd=input('请输入你的密码：')
            if len(pwd)<8:
                raise Exception('密码的长度不够，请输入一个8位以上的密码')
            except Exception as e:
                print(e)
        
        常见的异常类型；
        1.ZeroDivisionError     除（或取模）零（所有数据类型）
        2.IndexError     序列中没有此索引
        3.KeyError     映射中没有这个键
        4.NameError     未声明/初始化对象（没有属性）
        5.SyntaxError     python语法错误
        6.ValueError     传入无效的参数
        
        traceback模块
            使用traceback模块打印异常信息
            
            import traceback
            try:
                print('---------')
                num=1/0
            except:
                traceback.print_exc()
                
"""