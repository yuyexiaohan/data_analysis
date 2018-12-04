# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def myfont_set():
	"""中文配置"""
	font_path = "../numpy_exercise/msyh.ttc"
	my_font = font_manager.FontProperties(fname=font_path)
	return my_font

def draw_plot_fig(x, y, step, rotation, gd, file_path,*args):
	"""绘制折线图形"""
	plt.figure(figsize=(20,8), dpi=80)
	plt.plot(range(len(x)), y)
	plt.xticks(list(range(len(x)))[::step], x[::step].astype(int), rotation=rotation, fontproperties=myfont_set())
	# 判断是否添加栅格
	if gd:
		plt.grid()
	else:
		pass
	plt.savefig(file_path) # 先保存，在展示，否则会存在图形保存为空白的情况
	plt.show()

"""
现在我们有2015到2017年25万条911的紧急电话的数据，请统计出出这些数据中不同类型的紧急情况的次数，如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
"""
df = pd.read_csv("./911.csv")

print(df.head(5))
# 获取分类
# print()df["title"].str.split(": ")
temp_list = df["title"].str.split(": ").tolist()
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)
"""
         lat        lng ...                        addr  e
0  40.297876 -75.581294 ...      REINDEER CT & DEAD END  1
1  40.258061 -75.264680 ...  BRIAR PATH & WHITEMARSH LN  1
2  40.121182 -75.351975 ...                    HAWS AVE  1
3  40.116153 -75.343513 ...          AIRY ST & SWEDE ST  1
4  40.251492 -75.603350 ...    CHERRYWOOD CT & DEAD END  1

[5 rows x 9 columns]
"""

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

# 赋值
for cate in cate_list:
	zeros_df[cate][df["title"].str.contains(cate)] = 1
	# break
# print(zeros_df)

sum_ret = zeros_df.sum(axis=0)
print(sum_ret)
"""
['Fire', 'EMS', 'Traffic']
Fire        37432.0
EMS        124844.0
Traffic     87465.0
dtype: float64
"""
