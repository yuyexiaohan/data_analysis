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

