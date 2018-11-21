# coding=utf-8 
# Time : 2018/11/21 13:02 
# Author : achjiang
# File : test10_不同组距的直方图.py
from matplotlib import pyplot as plt
from matplotlib import font_manager

"""
在美国2004年人口普查发现有124 million的人在离家相对较远的地方工作。
根据他们从家到上班地点所需要的时间,通过抽样统计(最后一列)出了下表的数据,
这些数据能够绘制成直方图么?
"""

# 数据
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

# 中文设置
my_font = font_manager.FontProperties(fname='./msyh.ttc')

# 绘制图形
plt.figure(figsize=(20,8), dpi=80)  # 设置图形大小
plt.bar(range(len(quantity)), quantity, width=1)

# 设置x轴
_x  = [i-0.5 for i in range(len(quantity)+1)]
# 打印：[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]
_xtick_labels = interval + [150]
plt.xticks(_x, _xtick_labels)   # x轴的组距，按照_xtick_labels表明

# 栅格
plt.grid(linestyle='--')

# 保存
plt.savefig('./10不同组距的直方图')

# 图形展示
plt.show()

#
