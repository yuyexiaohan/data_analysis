# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
import pandas as pd
import numpy as np


"""
现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？

思路：遍历一遍，每次加1 ？？？
"""

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
grouped = df.groupby(by="Country")
# print(grouped)


# DataFrameGroupBy
# 可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)
# df[df["Country"]="US"]


# 1.调用聚合方法
country_count = grouped["Brand"].count() # 统计数量
# print(country_count["US"]) # 13608
# print(country_count["CN"]) # 2734


# 2.统计中国每个省店铺的数量
# china_data = df[df["Country"] =="CN"]
#
# grouped = china_data.groupby(by="State/Province").count()["Brand"]

# print(grouped)
"""
State/Province
11    236
12     58
13     24
14      8
15      8
21     57
22     13
23     16
31    551
32    354
33    315
34     26
35     75
36     13
37     75
41     21
42     76
43     35
44    333
45     21
46     16
50     41
51    104
52      9
53     24
61     42
62      3
63      3
64      2
91    162
92     13
Name: Brand, dtype: int64
"""

# 3.数据按照多个条件进行分组,返回Series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped)) # <class 'pandas.core.series.Series'>

# 4.数据按照多个条件进行分组,返回DataFrame
# df[["Brand"]]使用两个方括号，取里面具体的一维数组
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped2= df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]

print(grouped1,type(grouped1))
print("*"*100)
print(grouped2,type(grouped2))
print("*"*100)
print(grouped3,type(grouped3))

# 5.索引的方法和属性
# print(grouped1.index)

# 获取index：df.index
# 指定index ：df.index = ['x','y']
# 重新设置index : df.reindex(list("abcedf"))
# 指定某一列作为index ：df.set_index("Country",drop=False)
# 返回index的唯一值：df.set_index("Country").index.unique()
