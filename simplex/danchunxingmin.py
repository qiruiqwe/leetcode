import numpy as np


def pivot(zjcj, d):
    l = list(zjcj)
    jnum = l.index(max(l))  # 转入编号
    m = []
    for i in range(bn):
        if d[i][jnum] <= 0:
            m.append(0.)
        else:
            m.append(d[i][-1] / d[i][jnum])
    inum = m.index(min([x for x in m[1:] if x != 0]))  # 转出下标
    s[inum - 1] = jnum  # 更新基变量
    # 初等行列式变换，更新d
    r = d[inum][jnum]
    d[inum] /= r
    for i in [x for x in range(bn) if x != inum and x > 0]:
        r = d[i][jnum]
        d[i] -= r * d[inum]
    # 重新计算判别数
    # step1. CB?
    CB = []  # 进入的c
    for i in range(len(s)):
        CB.append(d[0][s[i]])
    # step. 计算每个变量的判别数
    zjcj = []
    for i in range(cn - 1):
        pj = d[1:, i]  # 修改
        zj = 0
        for j in range(len(CB)):
            zj = zj + CB[j] * pj[j]
        zjcj.append(zj - d[0][i])  # 修改
    return zjcj


def solve(zjcj, d):
    flag = True
    while flag:
        if max(list(zjcj)) <= 0:  # 直至所有系数小于等于0
            flag = False
        else:
            zjcj = pivot(zjcj, d)


def printSol():
    objective = 0
    for i in range(cn - 1):
        if i in s:
            objective += (d[s.index(i) + 1][-1]*d[0][i])
            print("x" + str(i) + "=%.2f" % d[s.index(i) + 1][-1])
        else:
            print("x" + str(i) + "=0.00")
    print("objective is %.2f" % objective)


if __name__ == '__main__':
    d = np.loadtxt("data-3.1.2.txt", dtype=np.float)
    (bn, cn) = d.shape
    s = list(range(cn - bn, cn - 1))  # 基变量列表
    zjcj = []
    for i in range(cn):
        zjcj.append(d[0][i] * -1)
    solve(zjcj, d)
    printSol()
