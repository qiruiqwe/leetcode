# @Time : 2020/11/22 14:51
# @Author : 亓瑞
# @File : userLogin.py
# @desc :
# 1) 输入用户名，如果不存在的话，要求重新输入，三次输入机会都用完，还没有输入正确用户名，程序退出;
# 2) 某个用户名输入正确，要求输入密码，如果密码输入不正确，要求将该密码存入当前的用户名账号里，再次输入此密码，登陆成功；
# 3）允许由多个用户可登陆此系统，每个用户可以有多个密码；
# 4）要求在自定义函数完成此功能，调用自定义函数实现用户登录功能；
# 5）要求有异常检测，用户名和密码可以放在文件里（在左侧自己上传存放用户和密码的文件，文件类型自己决定）
# 6) 上述为基本功能，大家可以发挥创意，实现更有意义的应用
import numpy as np

# 1.数据加载,如果没有找不到文件，那么使用初始数据
try:
    user = np.load('user.npy', allow_pickle=True).item()
except IOError:
    print("Error：no find .npy! Using init data！")
    user = {
        "qirui": ["123456"],
        "www": ["wen", "qi"]
    }
error = 0
while error < 3:
    print("please input username:")
    name = input()
    if name in user.keys():
        # 2.账号输入正确
        print("please input password:")
        password = input()
        if password in user[name]:
            # 2.1 密码输入正确
            print("login!")
            break
        else:
            # 2.2 密码输入错误，添加密码
            user[name].append(password)
    else:
        # 3.账号输入错误
        error = error + 1
        print("username error!")
# 4.保存数据
np.save('user.npy', user)