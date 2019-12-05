# -*- coding: utf-8 -*-
# @File  : learn_NumPy.py
# @Author: Freezinghot
# @Date  : 2019/12/1
# @Desc  : 学习NumPy科学计算库

# 查看NumPy版本
import numpy
print(numpy.__version__)

# 初识-通过np.random.random(4)生成一个浮点数组，类型为numpy.ndarray，长度为4
import numpy as np
a = np.random.random(4)
print(type(a))

print(a.shape)

print(a)

# 数据类型操作
# 指定数据类型
print(np.array(5, dtype=int))
print(np.array(5).astype(float))

# 转换数据类型
print(float(42))
print(bool(42))
print(float(True))

# 查看NumPy数据类型
print(set(np.typeDict.values()))

# numpy.array创建数组
a = np.array([[1, 2], [4, 5, 7]])
print(type(a))
print(a)

# range函数创建数组案例
a = range(0, 4)
b = range(4)
a1 = [i for i in a]
b1 = [i for i in b]
print(type(a))
print(a1)
print(b1)

# arange函数创建数组案例
a = np.arange(12)
print(a)
a2 = np.arange(1, 2, 0.1)
print(a2)

# linspace生成等差数列
a3 = np.linspace(start=1, stop=5, num=10, endpoint=True)
print(a3)
print(a3.shape)
b3 = np.linspace(start=1, stop=5, num=10, endpoint=False)
print(b3)
print(b3.shape)
c3 = np.linspace(start=1, stop=5, num=10,)
print(c3)

# logspace生成等比数列
# 生成首位是10的0次方，末位是10的2次方，含有5个数的等比数列
a4 = np.logspace(start=0, stop=2, num=5)
print(a4)
# 生成首位是1的0次方，末位是1的2次方，含有5个数的等比数列（base默认为10）
b4 = np.logspace(start=0, stop=2, num=5, base=1)
print(b4)

# ones案例-创建全1的数组
a5 = np.ones(4)
b5 = np.ones((4,), dtype=np.int)
c5 = np.ones((2, 1))
S = (2, 2)
d5 = np.ones(S)
# V = np.array([[1, 2, 3], [4, 5, 6]])
e5 = np.ones_like(a5)
print("a5={}\nb5={}\nc5={}\nd5={}\ne5={}".format(a5, b5, c5, d5, e5))

# zeros案例-创建全0的数组
a6 = np.zeros(5)
b6 = np.zeros((5,), dtype=np.int)
c6 = np.zeros((2, 1))
S = (2, 2)
d6 = np.zeros(S)
e6 = np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')])  # int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
x = np.arange(6)
x = x.reshape((2, 3))  # reshape重塑数组的形状
f = np.zeros_like(x)
y = np.arange(3, dtype=np.float)
g = np.zeros_like(y)
print("a6={}\nb6={}\nc6={}\nd6={}\ne6={}\nf={}\ny={}\ng={}".format(a6, b6, c6, d6, e6, f, y, g))

# empty根据给定形状和类型，返回一个空数组
a7 = np.empty([2, 4])
b7 = np.empty([2, 2], dtype=int)
temp = np.array([[1., 2., 3.], [4., 5., 6.]])
c7 = np.empty_like(temp)
print("a7={}\nb7={}\nc7={}".format(a7, b7, c7))

# eye(N, M=None, k=0, dtype=float)根据给定参数，生产第k个对角线元素为1、其他元素为0的数组
a8 = np.eye(2, dtype=int)
b8 = np.eye(3, 4, dtype=int)
c8 = np.eye(3, k=1)   # k默认0，生产主对角线元素为1；k为正指主对角线上移对应数；k为负指主对角线下移对应数
print("a8={}\nb8={}\nc8{}".format(a8, b8, c8))

# identity(n, dtype=None)建立n维单位方阵
a9 = np.identity(3)
print(a9)

# 索引：通过下表索引找到对应的存储空间
a10 = np.arange(1, 6)
# 使用正数作为索引
print(a10[3])
# 使用负数作为索引
print(a10[-4])
# 方括号中传入索引值，可同时选择多个元素
print(a10[[0, 3, 4]])

# 切片[start:stop:step]：通过下标或下标范围获得一组序列的元素
a11 = np.arange(16)      # 创建一维数组[0……15]
a11 = a11.reshape(4, 4)  # 更改数组形状
print(a11)
print(a11[1][2])       # 第2行第3列  ！！输出元素
print(a11[1, 2])       # 第2行第3列

print(a11[1:])         # 第2行及以下行 ！！输出数组
print(a11[:3])         # 第3行及以上行
print(a11[::2])        # 步进2，隔行输出
print(a11[1:2])        # 第2行
print(a11[1:2, 2:3])   # 第2行，第3列  ！！输出数组，与a11[1][2]输出不同

# 布尔型索引，又叫花式索引，利用整数数组进行索引
a12 = (np.arange(16)).reshape(4, 4)  # 生成4*4数组
x = np.array([0, 1, 2, 1])
x == 1    # 通过比较运算得到一个布尔数组
print(a12)
print(x == 1)          # x==1时为True
print(a12[x == 1])     # 输出True的行
print(a12[:, x == 1])  # 输出True的列

print(a12[x != 1])     # ！取反，x！=1时为True
print(a12[~(x == 1)])  # ~取反，x！=1时为True
print(a12[np.logical_not(x == 1)])  # logical_not()表示取否定
# 多条件组合布尔索引
print(a12[(x == 1) | (x == 2)])

# 利用布尔型索引实现图像分割
import matplotlib.pyplot as plt
a13 = np.linspace(0, 2 * np.pi, 200)    # 产生[0,2pi]之间的200点行线性的矢量
b13 = np.sin(a13)                       # 产生正弦曲线
plt.plot(a13, b13)                      # 绘制以a为横坐标，b为纵坐标的图像
mask = b13 >= 0                         # b>=0
plt.plot(a13[mask], b13[mask], 'bo')    # 绘制b>=0的部分，bo——蓝色圆点
mask = (b13 >= 0) & (a13 <= np.pi / 2)  # b>=0且a<=pi/2
plt.plot(a13[mask], b13[mask], 'go')    # 绘制b>=0且a<=pi/2的部分，go——绿色圆点
plt.show()
