# -*- coding: utf-8 -*-
# @File  : learn_dict.py
# @Author: Freezinghot
# @Date  : 2019/11/28
# @Desc  : 字典类型dict学习
## 初始化一个dict类型变量
x = {"a":1,"b":2,"c":3}
print (x)
## 读取x中的一个元素，直接读取或使用get方法
print (x["a"],",",x.get("a"))
## 使用get的方法返回none值：可在get方法中使用默认值
print (x.get("d"))
print (x.get("d","No such key"))
## 修改dict
x["c"] = 4
## 插入新的键值对
x["d"] = 5
del x["c"]
print(x)
