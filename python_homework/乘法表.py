# @Time : 2020/11/22 15:56
# @Author : 亓瑞
# @File : 乘法表.py
# @desc : 9 * 9 乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%2d * %2d = %2d" % (i, j, i*j), end=' ')
    print('\n')