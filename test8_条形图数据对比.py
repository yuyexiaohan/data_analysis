# coding=utf-8 
# Time : 2018/11/21 10:58 
# Author : achjiang
# File : test8_条形图数据对比.py
from matplotlib import pyplot as plt
from matplotlib import font_manager


"""
假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]
"""

# 条形图的排序

# 字体
my_font = font_manager.FontProperties(fname='./msyh.ttc')

# 数据
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

x_14 = list(range(len(a)))      # 4个元素：0，1，2，3
x_15 = [i+0.3 for i in x_14]    # 4个元素：0.3，1.3，2.3，3.3
x_16 = [i+0.3 for i in x_15]    # 4个元素：0.6，1.6，2.6，3.6

# 设置图形大小
plt.figure(figsize=(20,8), dpi=80)

# 绘制图形
# plt.bar(range(len(a)), b_14, width=0.3, color='blue')
# plt.bar(x_15, b_15, width=0.3, color='red')
# plt.bar(x_16, b_16, width=0.3, color='pink')
plt.bar(range(len(a)), b_14, width=0.3, label='9月14日票房')
plt.bar(x_15, b_15, width=0.3, label='9月15日票房')
plt.bar(x_16, b_16, width=0.3, label='9月16日票房')

# 设置图例
plt.legend(prop=my_font)

# 设置x轴，x_15是x轴位置，这里取x_15是将坐标轴数据放在中间，
# a是x轴的内容
plt.xticks(x_15, a, fontproperties=my_font)

# 保存
plt.savefig('./8条形图数据对比.png')

# 展示
plt.show()