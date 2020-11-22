# @Time : 2020/11/22 20:31
# @Author : 亓瑞
# @File : 收视变化.py
# @desc : 绘制东方卫视收视率变化趋势
import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.font_manager as font_manager
import pandas as pd

# 显示matplotlib生成的图形
# %matplotlib inline
# 请在下面cell中对东方卫视和浙江卫视的《平凡的荣耀》收视率变化趋势进行绘制，并进行分析

df = pd.read_json('work/viewing_infos.json', dtype={'broadcastDate': str})
broadcastDate_list = df['broadcastDate']
dongfang_rating_list = df['dongfang_rating']
zhejiang_rating_list = df['zhejiang_rating']

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.figure(figsize=(15, 8))
plt.title("《平凡的荣耀》东方卫视和东方卫视收视率变化趋势", fontsize=20)
plt.xlabel("播出日期", fontsize=20)
plt.ylabel("收视率%", fontsize=20)
plt.xticks(rotation=45, fontsize=20)
plt.yticks(fontsize=20)
plt.plot(broadcastDate_list, dongfang_rating_list)
plt.plot(broadcastDate_list, zhejiang_rating_list)
plt.grid()
plt.savefig('reuslt02.jpg')
plt.show()
