# -*- coding: utf-8 -*-
# @File  : learn_filter.py
# @Author: Freezinghot
# @Date  : 2019/11/30
# @Desc  : filter函数，筛选符合条件的元素
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)
