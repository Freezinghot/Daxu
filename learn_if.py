# -*- coding: utf-8 -*-
# @File  : learn_if.py
# @Author: Freezinghot
# @Date  : 2019/11/30
# @Desc  : 学习if条件语句
# if多条件
num = 3
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

# 三元运算
a = 1
b = 2
c = a-b if a>b else a+b
print(c)
