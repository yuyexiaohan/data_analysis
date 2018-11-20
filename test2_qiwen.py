# coding=utf-8 
# Time : 2018/11/20 20:07 
# Author : achjiang
# File : test2_qiwen.py
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


# 设置字体方式1：windows/linux设置字体方式
font = {
	'family': 'MicroSoft YaHei',
    'weight': 'bold',
    'size': 'larger'
	}
# matplotlib.rc('font',**font)
matplotlib.rc('font', family='Microsoft YaHei', weight='bold')

# 设置字体方式2：设置系统自带字体--family=''引号中为系统带字体的路径，可以使用fc-list 命令查看
my_font = font_manager.FontProperties(family='')

y = [random.randint(20, 35) for i in range(120)]
x = [i for i in range(120)]

# 设置图片大小
plt.figure(figsize=(16, 9), dpi=80)

# 绘图
plt.plot(x, y)

# 调整x轴的刻度
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45) # rotation旋转角度
# plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproparties=my_font) # rotation旋转角度 fontproparties是字体路径

# 添加描述信息
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度', fontproperties=my_font)
plt.title('10点到12点每分钟的气温变化情况', fontproperties=my_font)


# 保存
# plt.savefig('./2.png')

# 展示图形
plt.show()