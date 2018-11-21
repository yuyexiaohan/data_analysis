# coding=utf-8 
# Time : 2018/11/21 8:51 
# Author : achjiang
# File : test5_绘制散点图.py
from matplotlib import pyplot as plt
from matplotlib import font_manager


"""
假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温
(分别位于列表a,b),那么此时如何寻找出气温和随时间(天)变化的某种规律?

"""

# 坐标轴数据
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1,32)
x_10 = range(50,81)

# 中文字体路径被指
my_font = font_manager.FontProperties(fname='./msyh.ttc') # ''中配置系统的文字路劲

# 设置图形大小
plt.figure(figsize=(20,8), dpi=80)

# 绘图-散点图-和折线图的唯一区别
plt.scatter(x_3, y_3, label='3月')
plt.scatter(x_10, y_10, label='10月')

# 设置图例
plt.legend(prop=my_font)

# 调整x轴的刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ['3月{}日'.format(i) for i in x_3]
_xtick_labels += ['10月{}日'.format(i-49) for i in x_10]

plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加描述信息
plt.title('3月及10月天气统计图', fontproperties=my_font)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('天气温度/℃', fontproperties=my_font)

# 保存
plt.savefig('./5散点图.png')

# 展示
plt.show()


