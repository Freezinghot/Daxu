# -*- coding: utf-8 -*-
# @File  : learn_NumPy_linalg.py
# @Author: Freezinghot
# @Date  : 2019/12/16
# @Desc  : 矩阵运算与线性代数，主要介绍numpy，linalg函数(linalg = linear + algebra)
# 范数计算P63
import numpy as np
x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
# 默认参数ord=None,axis=None,keepdims=False
print("默认参数（矩阵二范数，不保留矩阵二维特性）：", np.linalg.norm(x))
print("矩阵二范数，保留矩阵二维特性：", np.linalg.norm(x, keepdims=True))
print("矩阵每个行向量，求向量的二范数：", np.linalg.norm(x, axis=1, keepdims=True))
print("矩阵每个列向量，求向量的二范数：",np.linalg.norm(x, axis=0, keepdims=True))
print("矩阵一范数：", np.linalg.norm(x, ord=1, keepdims=True))
print("矩阵二范数：", np.linalg.norm(x, ord=2, keepdims=True))
print("矩阵∞范数：", np.linalg.norm(x, ord=np.inf, keepdims=True))
print("矩阵每个行向量，求向量的一范数：", np.linalg.norm(x, ord=1, axis=1, keepdims=True))

# 用np.linalg.inv()求矩阵的逆
a = np.mat("0 1 2;1 0 3;4 -3 8")
a_inv = np.linalg.inv(a)
print("a=\n{}".format(a))
print("a_inv=\n{}".format(a_inv))
print("a*a_inv=\n{}".format(a*a_inv))

# 用np.linalg.solve()求方程组的解:3x+y=9;x+2y=8.
a1 = np.array([[3, 1], [1, 2]])
b1 = np.array([9, 8])
x = np.linalg.solve(a1, b1)
print("x={}".format(x))
# 使用dot函数检查求得的解是否正确
print(np.dot(a1, x))

# 用np.linalg.det()计算矩阵行列式
a2 = np.array([[1, 2], [3, 4]])
print("a2的行列式是{}".format(np.linalg.det(a2)))
# 多维数组计算行列式
a3 = np.array([[[1, 2], [3, 4]],[[1, 2], [2, 1]], [[1, 3], [3, 1]]])
print("a3数组的类型是{}".format(a3.shape))
print("a3的行列式是{}".format(np.linalg.det(a3)))

# 用numpy.linalg.lstsq(A, B)[0]最小二乘求解线性函数
x1 = np.array([0, 1, 2, 3])    # 注意：逗号分隔，是4*1的列矩阵
y1 = np.array([-1, 0.2, 0.9, 2.1])
A = np.vstack([x1, np.ones(len(x1))]).T  # np.ones(len())为常数项构建，此处构建与x1等长的全1矩阵
print("A={}".format(A))
m, c = np.linalg.lstsq(A, y1)[0]
print(m, c)
# 绘图
import matplotlib.pyplot as plt
plt.plot(x1, y1, 'o', label='Original data', markersize=10)
plt.plot(x1, m*x1 + c, 'r', label='Fitted line')
plt.legend()
plt.show()
