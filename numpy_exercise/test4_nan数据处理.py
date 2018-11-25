# coding=utf-8 
# Time : 2018/11/25
# Author : achjiang
import numpy as np


def fill_ndarray(t1):
	"""替换nan值"""
	for i in range(t1.shape[1]): # 遍历每一列
		temp_col = t1[:,i] # 当前的这一列
		nan_num = np.count_nonzero(temp_col!=temp_col) # 利用numpy中nan不等于nan的特性，使用不等于时，就是真来统计个数
		if nan_num !=0: # 不为0时，说明当前这一列中有nan
			# 当前这一列不为nan的array
			temp_not_nan_col = temp_col[temp_col==temp_col]
			# 选中当前为nan的位置，吧值赋值为不为nan的均值
			temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean() # mean是平均值
			print(t1.shape[1], i, temp_not_nan_col.mean())
			"""打印结果：
			4 2 6.0
			4 3 7.0
			"""
	return t1

if __name__ == '__main__':
	t1 = np.arange (12).reshape (3, 4).astype ('float')
	t1[1, 2:] = np.nan  # 替换为nan
	print (t1)
	"""打印结果：
	[[ 0.  1.  2.  3.]
	 [ 4.  5. nan nan]
	 [ 8.  9. 10. 11.]]
	"""
	t1 = fill_ndarray(t1)
	print (t1)
	"""打印结果：
	[[ 0.  1.  2.  3.]
	 [ 4.  5.  6.  7.]
	 [ 8.  9. 10. 11.]]
	"""

# 2 练习
"""
英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图

希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
"""
import matplotlib.pyplot as plt
from matplotlib import font_manager


# 中文字体路径被指
my_font = font_manager.FontProperties(fname='./msyh.ttc') # ''中配置系统的文字

us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")


# 获取评论数据
t_us_comments = t_us[:,-1]
t_uk_comments = t_uk[:,-1]


# 实际数据都集中在5000左右，所以将去除比5000小的地方
t_us_comments = t_us_comments[t_us_comments<=5000]
t_uk_comments = t_uk_comments[t_uk_comments<=5000]

# 绘图
# 查看数据的最大值最小值
print(t_us_comments.max(), t_us_comments.min()) # 582624 0
print(t_uk_comments.max(), t_uk_comments.min()) # 582624 0

d = 82

bin_nums_us = (t_us_comments.max()-t_us_comments.min())//d
bin_nums_uk = (t_uk_comments.max()-t_uk_comments.min())//d

# 绘图
# 1 绘制各国评论量的直方图
plt.figure(figsize=(20,8),dpi=80)
plt.hist(t_us_comments, bin_nums_us, label='美国')
plt.hist(t_uk_comments+5500, bin_nums_uk, label='英国')



plt.title('youtube用户分类', fontproperties=my_font)
plt.xlabel('用户数量', fontproperties=my_font)
plt.ylabel('评论数量', fontproperties=my_font)

# 设置图例
plt.legend(prop=my_font)

# 栅格
plt.grid()

# 保存
plt.savefig("./11nan数据直方图.png")

# 图形展示
plt.show()

