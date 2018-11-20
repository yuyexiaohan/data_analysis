# coding=utf-8 
# Time : 2018/11/20 22:52 
# Author : achjiang
# File : test3_3.py
from matplotlib import pyplot as plt
from matplotlib import font_manager


"""
展示一个人11-31岁期间每年交女朋友的数量
"""
x = range(11, 31)
y = [1,0,0,1,2,3,4,1,2,1,1,0,0,1,2,3,4,1,2,1,]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图形
plt.plot(x, y)

# 设置x轴刻度
_xtick_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_labels, )

# 绘制栅格
plt.grid()

# 添加图例
plt.legend()

# 保存
plt.savefig('./3.png')

# 展示
plt.show()


