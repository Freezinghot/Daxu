# -*- coding: utf-8 -*-
# @File  : learn_lambda.py
# @Author: Freezinghot
# @Date  : 2019/11/29
# @Desc  : 学习lambda表达式和常用内置函数
# 用def定义函数


def f(a, b):
    return a + b


print(f(1, 2))
# 用lambda定义函数
g = lambda x, y: x + y
print(g(1, 2))

# 内置map函数和lambda表达式
# 1是一个0~5的列表
lb = range(6)
print(lb)

# 生成一个新的列表，列表里的元素为lb里的元素加1


def addone(data):
    re = []
    for i in data:
        re.append(i + 1)
    return re


print(addone(lb))

# 通过内置的map函数和lambda表达式实现上述结果
# 在python3里面，map()的返回值已经不再是list,而是iterators, 所以想要使用，只用将iterator 转换成list 即可,比如list(map())
print(map(lambda x: x + 1, lb))

# 同样功能的列表生产式
print([i + 1 for i in lb])

# 计算ld中每个元素的两倍和平方，并将两种组成一个列表
# lambda表达式和python函数一样，也可以接受函数作为参数
twotimes = lambda x: x * 2
square = lambda x: x ** 2
print([list(map(lambda x: x(i), [twotimes, square])) for i in lb])

# 内置filter函数，选择lb中的偶数
# 仍需要用list转换输出格式
print(list(filter(lambda x: x % 2 == 0, lb)))

# 内置reduce函数，计算lb的和
# python3中使用reduce需要先加载functools
from functools import reduce
print(reduce(lambda accumValue, newValue: accumValue + newValue, lb, 0))
