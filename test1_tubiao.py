# coding=utf-8 
# Time : 2018/11/20 19:23 
# Author : achjiang
# File : test1_tubiao.py

from matplotlib import pyplot as plt


x = range(2, 26, 2)
y = [15,13,14,5,17,20,33,34,35,36,29,20]

# 设置图片大小
# plt.figure(figsize=(16, 9), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴的刻度
plt.xticks(x)

# 保存
plt.savefig('./1.png')

# 展示图形
plt.show()