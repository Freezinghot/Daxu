# -*- coding: utf-8 -*-
# @File  : learn_list.py
# @Author: Freezinghot
# @Date  : 2019/11/28
# @Desc  : 学习list列表类型操作
# 初始化一个list类型变量y
y = ["A", "B", "C", "a", "b", "c"]
print(y)
# 读取y中的元素
print(y[0])
print(y[-1])
print(y[0:3])
# 查找y中的元素
print(y.index("a"))
# 修改list
y[0] = 4
print(y)
# 在y的最后插入新元素
y.append(5)
print(y)
# 在指定位置插入新元素
y.insert(3, "new")
print(y)
# 两个list合并，注意和append的区别
print(y + ["d", "e"])
y.append(["d", "e"])
print(y)
# 删掉y里的元素
y.remove("B")
print(y)
