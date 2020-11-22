# @Time : 2020/11/22 16:30
# @Author : 亓瑞
# @File : 解压文件.py
# @desc :
# 1、将data文件夹下的zip文件解压，将image文件夹放到work文件夹下
# 2. work/image文件夹中的所有文件进行重命名，在文件名前加入“new_”,如将“1.jpg”重命名为“new_1.jpg”
import os
# 1.获取当前位置
cwd = os.getcwd()
cwd = cwd + '\image'
print("目录为:", os.listdir(cwd))
# 2.对目录中的每个文件夹遍历
for i in os.listdir(cwd):
    current_cwd = cwd + "\\" + i
    print('%s', os.listdir(current_cwd))
    # 3.对文件夹中的。jpg进行修改
    for j in os.listdir(current_cwd):
        src = current_cwd + "\\" + j
        target = current_cwd + "\\new_" +j
        os.renames(src, target)
# print(cwd)


