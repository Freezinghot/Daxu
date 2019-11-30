# -*- coding: utf-8 -*-
# @File  : learn_while.py
# @Author: Freezinghot
# @Date  : 2019/11/30
# @Desc  : 学习循环语句
# while循环
count = 0
while(count < 9):
    print('The count is:', count)
    count = count + 1
print("Good bye!")


# for循环
for i in range(5):
    print("i=%d" % i)

# break跳出循环
for i in range(5):
    if i == 3:
        break
    print("i=%d" % i)

# continue语句——终止本次循环，但不跳出
for j in range(5):
    if j == 3:
        continue
    print("j=%d" % j)


# pass填充，用于填充没有想好的程序，使其正常运行
def sample():

    pass
