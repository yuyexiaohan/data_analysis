# coding=utf-8 
# Time : 2018/11/25
# Author : achjiang

"""
英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图

希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


# 中文字体路径被指
my_font = font_manager.FontProperties(fname='./msyh.ttc') # ''中配置系统的文字

us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

t_uk = t_uk[t_uk[:,1]<=500000]
t_uk_comments = t_uk[:,-1]

t_uk_like = t_uk[:, 1]

# 2 绘制评论量和喜欢量的散点图
plt.scatter(t_uk_like,t_uk_comments)


plt.title('youtube用户评论和喜欢情况', fontproperties=my_font)
plt.xlabel('评论数量', fontproperties=my_font)
plt.ylabel('喜欢数量', fontproperties=my_font)

# 设置图例
plt.legend(prop=my_font)

# 栅格
plt.grid()

# 保存
plt.savefig("./12评论数与喜欢数的散点图.png")

# 图形展示
plt.show()
