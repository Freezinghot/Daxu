# -*- coding: utf-8 -*-
# @File  : learn_formatout.py
# @Author: Freezinghot
# @Date  : 2019/11/29
# @Desc  : 格式化输出学习

# %操作符，可实现字符串格式化
print("%o" % 10)
print("%d" % 10)
print("%f" % 10)
print("%.2e" % 10)
print("%.2g" % 10)
print("%f" % 3.141592653)
print("%.2f" % 3.141592653)
# round函数:round(数字表达式，小数位数）
print(round(3.141592653 * 2 + 1, 3))
# format格式化字符串
# format按位置输出
print("{} {}".format("hello", "world"))
print("{0} {0} {1}".format("hello", "world"))
# format索引输出
str = "hello"
list = ["hello", "world"]
tuple = ("hello", "world")
print("{0[1]}".format(str))
print("{0[0]}, {0[1]}".format(list))
print("{0[0]}, {0[1]}".format(tuple))

print("{p[1]}".format(p=str))
print("{p[0]}, {p[1]}".format(p=list))
print("{p[0]}, {p[1]}".format(p=tuple))

# format字典形式输出
Tom = {'age': 27, 'gender': 'M'}
print("{0[age]}".format(Tom))
print("{p[gender]}".format(p=Tom))

# format通过对象属性输出
# 注意：__init__两侧是两个下划线_

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{self.name} is {self.age} years old'.format(self=self)


print(Person('Tom', 18))

# 字符串对齐并指定对其宽度输出
print('默认输出：{}， {}'.format('hello', 'world'))
print('左右各取10位对齐：{:10s}， {:>10s}'.format('hello', 'world'))
print('取10位中间对齐：{:^10s}， {:^10s}'.format('hello', 'world'))
print('取2位小数：{} is {:.2f}'.format(3.141592,  3.141592))
print('数值的千位分割符：{} is {:,}'.format(123456789, 1234567890))

输出：
12
10
10.000000
1.00e+01
10
3.141593
3.14
7.283
hello world
hello hello world
e
hello, world
hello, world
e
hello, world
hello, world
27
M
Tom is 18 years old
默认输出：hello， world
左右各取10位对齐：hello     ，      world
取10位中间对齐：  hello   ，   world   
取2位小数：3.141592 is 3.14
数值的千位分割符：123456789 is 1,234,567,890
