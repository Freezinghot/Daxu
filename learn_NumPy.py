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

#################################
输出：
1.16.2
<class 'numpy.ndarray'>
(4,)
[0.04899119 0.88943573 0.12171455 0.20854629]
5
5.0
42.0
True
1.0
{<class 'numpy.float64'>, <class 'numpy.complex128'>, <class 'numpy.float16'>, <class 'numpy.bytes_'>, <class 'numpy.uint16'>, <class 'numpy.complex64'>, <class 'numpy.complex128'>, <class 'numpy.timedelta64'>, <class 'numpy.int32'>, <class 'numpy.uint8'>, <class 'numpy.float64'>, <class 'numpy.void'>, <class 'numpy.int64'>, <class 'numpy.uint32'>, <class 'numpy.object_'>, <class 'numpy.int8'>, <class 'numpy.int32'>, <class 'numpy.uint64'>, <class 'numpy.int16'>, <class 'numpy.uint32'>, <class 'numpy.str_'>, <class 'numpy.datetime64'>, <class 'numpy.float32'>, <class 'numpy.bool_'>}
<class 'numpy.ndarray'>
[list([1, 2]) list([4, 5, 7])]
<class 'range'>
[0, 1, 2, 3]
[0, 1, 2, 3]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
(10,)
[1.  1.4 1.8 2.2 2.6 3.  3.4 3.8 4.2 4.6]
(10,)
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
[  1.           3.16227766  10.          31.6227766  100.        ]
[1. 1. 1. 1. 1.]
a5=[1. 1. 1. 1.]
b5=[1 1 1 1]
c5=[[1.]
 [1.]]
d5=[[1. 1.]
 [1. 1.]]
e5=[1. 1. 1. 1.]
a6=[0. 0. 0. 0. 0.]
b6=[0 0 0 0 0]
c6=[[0.]
 [0.]]
d6=[[0. 0.]
 [0. 0.]]
e6=[(0, 0) (0, 0)]
f=[[0 0 0]
 [0 0 0]]
y=[0. 1. 2.]
g=[0. 0. 0.]
a7=[[6.23042070e-307 4.67296746e-307 1.69121096e-306 1.11258022e-307]
 [8.34441742e-308 1.42420481e-306 1.24612013e-306 3.91910665e+202]]
b7=[[         0 1072693248]
 [         0 1073741824]]
c7=[[1.99549395e+161 9.77824555e+199 6.01334653e-154]
 [6.01347002e-154 1.69375270e+190 2.35569008e+251]]
