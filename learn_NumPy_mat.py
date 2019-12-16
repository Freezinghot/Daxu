# -*- coding: utf-8 -*-
# @File  : learn_NumPy_mat.py
# @Author: Freezinghot
# @Date  : 2019/12/5
# @Desc  : 学习矩阵的合并与分割
# 矩阵合并
import numpy as np
a = np.floor(10*np.random.random((2, 2)))  # 生成10以内的数组成的2*2矩阵a
b = np.floor(10*np.random.random((2, 2)))
# vstack()上下（行）合并
c = np.vstack((a, b))
# hstack()左右（列）合并
d = np.hstack((a, b))
print("a=\n{}\nb=\n{}\nc=\n{}\nd=\n{}".format(a, b, c, d))

# 矩阵分割
from numpy import newaxis
# np.column_stack((a1, b1))
a1 = np.array([1, 2])
b1 = np.array([3, 4])
c1 = np.column_stack((a1, b1))  # 合并数组为一维时，column_stack()按列方向合并
d1 = np.hstack((a1, b1))        # hstack()只是将数组左右按列合并
print("a1=\n{}\nb1=\n{}\nc1=\n{}\nd1=\n{}".format(a1, b1, c1, d1))
# newaxis插入新的维度，由一维变成二维数组；
e1 = np.column_stack((a1[:, newaxis], b1[:, newaxis]))  # [:, newaxis]newaxis在后时，生成数组为(n*1)维；
f1 = np.column_stack((a1[newaxis, :], b1[newaxis, :]))  # newaxis在前时，生成数组为(1*n)维
g1 = np.hstack((a1[:, newaxis], b1[:, newaxis]))  # a1为2*1 ，b1为2*1，hstack合并后2*2
print("e1=\n{}\nf1=\n{}\ng1\n{}".format(e1, f1, g1))
