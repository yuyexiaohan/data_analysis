# coding=utf-8 
# Time : 2018/12/4
# Author : achjiang
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



"""
现在我们有2015到2017年25万条911的紧急电话的数据，请统计出出这些数据中不同类型的紧急情况的次数，如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
"""
df = pd.read_csv("./911.csv")

print(df.head(5))
#获取分类
# print()df["title"].str.split(": ")
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

# print(df.head(5))
print(df.groupby(by="cate").count()["title"])
"""
cate
EMS        124840
Fire        37432
Traffic     87465
Name: title, dtype: int64
"""
