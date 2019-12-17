# -*- coding: utf-8 -*-
# @File  : learn_linalg.lstsq.py
# @Author: Freezinghot
# @Date  : 2019/12/17
# @Desc  : 一个线性回归案例
xd = [18, 23, 25, 35, 65, 54, 34, 56, 72, 19, 23, 42, 18, 39, 37]  # 年龄
yd = [202, 186, 187, 180, 156, 169, 174, 172, 153, 199, 193, 174, 198, 183, 178]  # 最大心率
n = len(xd)
# 计算
import numpy as np
B = np.array(yd)
# A = np.array(xd)
A = np.array(([[xd[j], 1] for j in range(n)]))
X = np.linalg.lstsq(A, B)[0]
a = X[0]
b = X[1]
print("Line is:y=", a, "x+", b)
# 绘图
import matplotlib.pyplot as plt
plt.plot(np.array(xd), B, 'ro', label='Original data', markersize=10)
plt.plot(np.array(xd), a*np.array(xd) + b, label='Fitted line')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
