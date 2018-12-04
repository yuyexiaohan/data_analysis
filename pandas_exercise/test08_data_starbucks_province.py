# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib import font_manager

"""
使用matplotlib呈现出每个中国每个城市的店铺数量
"""

# 配置数据文件路径
file_path = './starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)

# 获取每个城市的店铺数据
df = df[df['Country']=='CN'] # 获取中国数据

# 店铺总数排名前25的城市，索引城市排序后切片前25个
data = df.groupby(by='City').count()['Brand'].sort_values(ascending=False)[:25]

# 配置中文字体文件路径
my_font = font_manager.FontProperties(fname="../numpy_exercise/msyh.ttc")

# 绘制图形
_x = data.index
_y = data.values
# 设置图形大小
plt.figure(figsize=(20,12), dpi=80)
# 画图
# plt.bar(range(len(_x)), _y, width=0.3, color='pink')
plt.barh(range(len(_x)), _y, height=0.3, color='pink')
# 设置x轴
# plt.xticks(range(len(_x)), _x, fontproperties=my_font)
# 设置y轴
plt.yticks(range(len(_x)), _x, fontproperties=my_font)

# 加栅格
plt.grid()
# 图形展示
plt.show()
# 保存图形
plt.savefig('./08_data_starbucks_province.png')
