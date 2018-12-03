# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
print(df["Genre"].head(3))
#统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()  #[[],[],[]]

genre_list = list(set([i for j in temp_list for i in j]))

#构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zeros_df)

#给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    #zeros_df.loc[0,["Sci-fi","Mucical"]] = 1
    zeros_df.loc[i,temp_list[i]] = 1

# print(zeros_df.head(3))

#统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)
print(genre_count)

#排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
#画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y,width=0.4,color="orange")
plt.xticks(range(len(_x)),_x)
plt.savefig('./05-sum-class.png')
plt.show()

# 合并
# 1. join 按照行索引进行合并
"""
In [7]: df1 = pd.DataFrame(np.ones((2,4)),index=['A','B'],columns=list('abcd'))

In [8]: df1
Out[8]:
     a    b    c    d
A  1.0  1.0  1.0  1.0
B  1.0  1.0  1.0  1.0

In [9]: df2 = pd.DataFrame(np.zeros((3,3)),index=['A','B','C'],columns=list('xyz'))

In [10]: df2
Out[10]:
     x    y    z
A  0.0  0.0  0.0
B  0.0  0.0  0.0
C  0.0  0.0  0.0

In [11]: df2.join(df1)
Out[11]:
     x    y    z    a    b    c    d
A  0.0  0.0  0.0  1.0  1.0  1.0  1.0
B  0.0  0.0  0.0  1.0  1.0  1.0  1.0
C  0.0  0.0  0.0  NaN  NaN  NaN  NaN
"""
# 2. merge按照列索引进行合并
"""
In [12]: df3 = pd.DataFrame(np.zeros((3,3)),columns=['f','a','x'])

In [13]: df3
Out[13]:
     f    a    x
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0

In [14]: df1.merge(df3,on='a')
Out[14]:
Empty DataFrame
Columns: [a, b, c, d, f, x]
Index: []

# 使用merge方法，df3与df1交集的是1,(0,a)是1，匹配2次。
# 当配置为1时，

In [25]: df3 = pd.DataFrame(np.arange(9).reshape((3,3)),columns=['f','a','x'])

In [26]: df3
Out[26]:
   f  a  x
0  0  1  2
1  3  4  5
2  6  7  8

In [27]: df1.merge(df3,on='a')
Out[27]:
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2

# 3.各类连接：
# 左连接：按照左边的df1为准
In [28]: df1.merge(df3,on='a',how='left')
Out[28]:
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2

# 右连接：按照右边的df3为准，右不同的在添加，其它没有的补nan
In [29]: df1.merge(df3,on='a',how='right')
Out[29]:
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2
2  4.0  NaN  NaN  NaN  3  5
3  7.0  NaN  NaN  NaN  6  8

# 内连接：and 交集操作
In [30]: df1.merge(df3,on='a',how='inner')
Out[30]:
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2

# 外连接: or 并集操作
In [31]: df1.merge(df3,on='a',how='outer')
Out[31]:
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2
2  4.0  NaN  NaN  NaN  3  5
3  7.0  NaN  NaN  NaN  6  8

"""