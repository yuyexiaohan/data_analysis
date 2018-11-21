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

# 设置字体方式2：设置系统自带字体--family=''引号中为系统带字体的路径，可以使用fc-list 命令查看
my_font = font_manager.FontProperties(fname='./msyh.ttc')

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图-折线图
plt.plot(x, y, label='路人甲', color='red')
plt.title('恋爱次数统计', fontproperties=my_font)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('恋爱次数', fontproperties=my_font)

# 添加图例
plt.legend(loc='upper left', prop=my_font)

# 设置x轴刻度
_xtick_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)

# 绘制栅格
plt.grid()

# 保存
plt.savefig('./3折线图.png')

# 展示
plt.show()
