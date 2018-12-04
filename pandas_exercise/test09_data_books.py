# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib import font_manager

"""
现在我们有全球排名靠前的10000本书的数据，那么请统计一下下面几个问题：
- 不同年份书的数量
- 不同年份书的平均评分情况
"""

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


# 获取数据
df = pd.read_csv('./books.csv')
# with open('./book.txt', 'w') as f:
# 	content = f.write(str(df.head()))
# print(df.info())
# print(df.head())

# 1.不同年份书的数量
# 获取年份数据
data = df[pd.notnull(df["original_publication_year"])]
group1 = df.groupby(by='original_publication_year').count()["title"]

# 2. 不同年份书的平均评分情况
group2 = data["average_rating"].groupby(by=data["original_publication_year"]).mean()

_x = group1.index
_y = group1.values
step = 10

_x2 = group2.index
_y2 = group2.values

fig1 = draw_plot_fig(_x, _y, step, rotation=45, gd=True, file_path="./09-01-books01.png")
fig2 = draw_plot_fig(_x2, _y2, step, rotation=45, gd=True, file_path="./09-01-books02.png")

