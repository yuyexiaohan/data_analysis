# coding=utf-8 
# Time : 2018/11/20 23:09 
# Author : achjiang
# File : test4_多条折线图.py
from matplotlib import pyplot as plt
from matplotlib import font_manager


"""
展示2个人11-31岁期间每年交女朋友的数量
"""
x = range(11, 31)
y_1 = [1,0,0,1,2,3,4,1,2,1,1,0,0,1,2,3,4,1,2,1,]
y_2 = [2,3,4,1,5,1,1,0,1,1,1,2,0,1,2,1,1,1,1,1,]
y_3 = [1,3,4,1,5,1,1,0,1,1,1,2,4,1,2,1,1,4,1,3,]

# 设置字体方式2：设置系统自带字体--family=''引号中为系统带字体的路径，可以使用fc-list 命令查看
my_font = font_manager.FontProperties(family='')

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图形
plt.plot(x, y_1, label='路人甲', color='orange', linestyle=':')
plt.plot(x, y_2, label='路人乙', color='blue', linestyle='--')
plt.plot(x, y_3, label='路人丙', color='#AFEEEE', linestyle='--')

# 设置x轴刻度
_xtick_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_labels, )

# 绘制栅格
plt.grid(linestyle='--')

# 添加图例
plt.legend(loc='upper left') # 将图示调整到左上角

# 坐标轴描述
plt.title('路人恋爱指数分布图', fontproperties=my_font)
plt.xlabel('时间/年', fontproperties=my_font)
plt.ylabel('恋爱次数/次', fontproperties=my_font)

# 保存
plt.savefig('./4.png')

# 展示
plt.show()


