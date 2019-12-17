# -*- coding: utf-8 -*-
# @File  : learn_linalg.eigvals.py
# @Author: Freezinghot
# @Date  : 2019/12/17
# @Desc  : 用numpy.linalg.eigvals()求特征值与特征向量
import numpy as np
# 创建一个矩阵
C = np.mat("3 -2;1 0")
# 调用eigvals函数求解特征值
c0 = np.linalg.eigvals(C)
print("特征值c0={}".format(c0))
# 使用eig函数求解特征值和特征向量
c1, c2 = np.linalg.eig(C)
print("特征值c1={}".format(c1))
print("特征向量c2={}".format(c2))
# 使用dot函数验证求得的解是否正确
for i in range(len(c1)):
    print("left:", np.dot(C, c2[:, i]))
    print("right:", c1[i]*c2[:, i])
