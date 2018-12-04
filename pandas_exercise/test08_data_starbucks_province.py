# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
from matplotlib import pyplot as plt
import pandas as pd

"""
使用matplotlib呈现出每个中国每个城市的店铺数量
"""

# 配置数据文件路径
file_path = './starbucks_store_worldwide.csv'
df = pd.read_csv(file_path)

# 获取每个城市的店铺数据
data = df.groupby()

# 绘制图形
