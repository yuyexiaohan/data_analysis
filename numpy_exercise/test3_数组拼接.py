# coding=utf-8 
# Time : 2018/11/21 23:51 
# Author : achjiang
# File : test3_数组拼接.py
import numpy as np


"""
现在希望把之前案例中两个国家的数据方法一起来研究分析，同时保留国家的信息（每条数据的国家来源），应该怎么办
"""

us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# 加载国家数据
us_data = np.loadtxt(us_file_path, delimiter=',', dtype=int)
uk_data = np.loadtxt(uk_file_path, delimiter=',', dtype=int)

# 田间国家信息
# 构造全为零的数据
zeros_data = np.zeros((us_data.shape[0], 1))
ones_data = np.ones((uk_data.shape[0], 1))

# 分别添加一列全为0，1的数组
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data,ones_data))

# 拼接两组数据
final_data = np.vstack((us_data, uk_data))
print(final_data)
"""
[[4.394029e+06 3.200530e+05 5.931000e+03 4.624500e+04 0.000000e+00]
 [7.860119e+06 1.858530e+05 2.667900e+04 0.000000e+00 0.000000e+00]
 [5.845909e+06 5.765970e+05 3.977400e+04 1.707080e+05 0.000000e+00]
 ...
 [1.092220e+05 4.840000e+03 3.500000e+01 2.120000e+02 1.000000e+00]
 [6.262230e+05 2.296200e+04 5.320000e+02 1.559000e+03 1.000000e+00]
 [9.922800e+04 1.699000e+03 2.300000e+01 1.350000e+02 1.000000e+00]]
"""
