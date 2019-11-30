# -*- coding: utf-8 -*-
# @File  : learn_map.py
# @Author: Freezinghot
# @Date  : 2019/11/30
# @Desc  : 学习map函数
seq_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
F = list(map(lambda x:x ** 2, seq_list))
print(F)
# 应用于多个列表
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [5, 6, 7]
ab = list(map(lambda x, y: x + y, a, b))
print(ab)
# 应用于多个列表不同元素,结果取决于最短列表
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [5, 6, 7]
ac = list(map(lambda x, y: x + y, a, c))
print(ac)
