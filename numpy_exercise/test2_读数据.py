# coding=utf-8 
# Time : 2018/11/21 22:27 
# Author : achjiang
# File : test2_读数据.py
import numpy as np


us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

t1 = np.loadtxt(us_file_path, delimiter=',', dtype=int, unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=',', dtype=int) # 转置之后数据

# print(t1)
# print(20*'*')
# print(t2)
"""打印结果：
[[4394029 7860119 5845909 ...  142463 2162240  515000]
 [ 320053  185853  576597 ...    4231   41032   34727]
 [   5931   26679   39774 ...     148    1384     195]
 [  46245       0  170708 ...     279    4737    4722]]
********************
[[4394029  320053    5931   46245]
 [7860119  185853   26679       0]
 [5845909  576597   39774  170708]
 ...
 [ 142463    4231     148     279]
 [2162240   41032    1384    4737]
 [ 515000   34727     195    4722]]
"""
# print(50*'*')
# # numpy的索引和切片
#
# # 取行
# print(t2[2]) # 索引
# print(50*'*')
# # 取连续行
# print(t2[2:])
# print(50*'*')
# # 取不连续的多行
# print(t2[[2,8,10]])
"""打印结果：
**************************************************
[5845909  576597   39774  170708]
**************************************************
[[5845909  576597   39774  170708]
 [2642103   24975    4542   12829]
 [1168130   96666     568    6666]
 ...
 [ 142463    4231     148     279]
 [2162240   41032    1384    4737]
 [ 515000   34727     195    4722]]
**************************************************
[[5845909  576597   39774  170708]
 [1338533   69687     678    5643]
 [ 859289   34485     726    1914]]
"""

# 取列
# print(t2[1,:])
# print(50*'*')
#
# print(t2[2,:])
# print(50*'*')
#
# print(t2[[2,10,3],:])
"""打印结果：
[7860119  185853   26679       0]
**************************************************
[5845909  576597   39774  170708]
**************************************************
[[5845909  576597   39774  170708]
 [ 859289   34485     726    1914]
 [2642103   24975    4542   12829]]
"""

# 取连续的多列
# print(t2[:,2:])
"""
[[  5931  46245]
 [ 26679      0]
 [ 39774 170708]
 ...
 [   148    279]
 [  1384   4737]
 [   195   4722]]
"""

# 取不连续的多列
print(t2[:,[0,2]])
"""
[[4394029    5931]
 [7860119   26679]
 [5845909   39774]
 ...
 [ 142463     148]
 [2162240    1384]
 [ 515000     195]]
"""

# 取行和列
# a = t2[2,3]
# print(a)
# print(type(a))
"""
[[4394029    5931]
 [7860119   26679]
 [5845909   39774]
 ...
 [ 142463     148]
 [2162240    1384]
 [ 515000     195]]
170708
<class 'numpy.int32'>
"""

# 取多行多列
# b = t2[2:5, 1:4]
# print(b, type(b))
"""
[[4394029    5931]
 [7860119   26679]
 [5845909   39774]
 ...
 [ 142463     148]
 [2162240    1384]
 [ 515000     195]]
[[576597  39774 170708]
 [ 24975   4542  12829]
 [ 96666    568   6666]] <class 'numpy.ndarray'>
"""

# 取不相邻的多个点
# 选出来的是（0，0） （2，1） （2，3）这三个点
c = t2[[0,2,2], [0,1,3]]
print(c)
"""
[[4394029    5931]
 [7860119   26679]
 [5845909   39774]
 ...
 [ 142463     148]
 [2162240    1384]
 [ 515000     195]]
[4394029  576597  170708]
"""