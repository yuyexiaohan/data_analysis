
### matplotlib如何使用，绘制折线图，matplotlib如何设置线条颜色和风格

  ```python
  from matplotlib import pyplot as plt
  #设置图形大小
  plt.figure(figsize=(20,8),dpi=80)
  plt.plot(x,y,color="cyan",linestyle="",linewidth="",alpha=0.4,label="")
  #设置网格
  plt.grid(alpha="",linestyle="")
  #设置图例
  plt.legend(loc="",prop=my_font)

  #设置图信息
  plt.xlabel("时间",fontproperties=my_font)
  plt.ylabel("时间",fontproperties=my_font)
  plt.title("",fontproperties=my_font)

  #保存
  plt.savefig("./baidu.png")
  plt.show()
  ````

### matplotlib如何设置x轴的刻度
  ```python
  #设置显示中文
  from matplotlib import font_manager
  my_font = font_manager.FontProperties(fname="")
  plt.xticks(x,["","",""],fontproperties=my_font,rotation=45)
  ```

### 常见统计图的对比
  - 折线图：展示数据的变化情况
  - 散点图：两个属性上的数据的相关情况，展示离群点
  - 直方图：统计连续的数据
  - 条形图：统计离散的数据

#### 四种图形使用情况对比
  - 观察变化的时候使用 折线图，plot
  - 观察不同维度之间的关系 散点图 ，scatter
  - 统计离散的数据  条形图 bar，barh
  - 统计连续的数据  直方图 hist

#### scatter
  - plt.scatter(x,y)

#### bar，barh
  - plt.bar(x,y,width=0.3）
  - plt.bar(x,y,height=0.3）

#### hist
  - plt.hist([1,2,3],组数)
  - 组数=（最大值-最小值）/ 组距

#### numpy
  - 创建数组
  > import numpy as np
  np.array([])
  np.array(range())
  np.arange(3,10,2)  #生成从3到10，步长为2的一个一维数组

  - 数据类型
  > int, float, "int64" ,"int32","float32",bool
  > t1.dtype  #观察数据类型
  > t1.astype()
  
  #### numpy的索引和切片
  - t[10,20]
  - `t[[2,5],[4,8]]`

  - t[3:]
  - t[[2,5,6]]

  - t[:,:4]
  - t[:,[2,5,6]]

  - t[2:3,5:7]


#### numpy中的bool索引,where,clip的使用
  - t[t<30] = 2
  - np.where(t<10,20,5)
  - t.clip(10,20)


#### 转置和读取本地文件
  - t.T
  - t.transpose()
  - t.sawpaxes()

  - np.loadtxt(file_path,delimiter,dtype)


#### nan和inf是什么
  - nan not a number
  - np.nan != np.nan
  - 任何值和nan进行计算都是nan

  - inf 无穷

#### 常用统计函数
  - t.sum()
  - t.mean()
  - np.meadian()
  - t.max()
  - t.min()
  - np.ptp()
  - t.std()

#### numpy数组的拼接
  - np.hstack(t1,t2)
  - np.vstack(t1,t2)

#### Series如何创建，如何进行索引和切片
  - pd.Series([])
  - pd.Series({})  #字典的键就是Series的索引

  - s1["a"]
  - `s1[["a","c"]]`
  - `s1[1]`
  - `s2[[1,5,3]]`
  - s2[4:10]


#### DataFrame如何创建，如何进行索引和切片
  - `pd.DataFrame([[],[],[]])` #接收2维数组
  - pd.DataFrame({"a":[1,23],"c":[2,3]})
  - pd.DataFrame([{},{},{}])


#### DataFrame缺失数据处理
  - 0
    - 并不是所有的都需要处理
    - df[df==0] = np.nan
  - nan
    - pd.isnan ，pd.notnan
    - df.dropna(axis=0,how="any[all]",inplace=True)
    - df.fillna(df.mean())
    - df["A"] = df["A"].fillna(df["A"].mean())

#### 字符串离散化进行统计
  - 获取分类去重后的列表
  - 构造全为0的DataFrame，形状是（数据的行数，分类列表的长度），列索引是分类去重后的列表
  - 遍历原始数据，对全为0的df赋值
    - zeros_df.loc[i,["T","M"]] = 1
  - 按列进行求和

#### join
  - 按照行索引进行合并

#### merge
  - 按照某一列进行和并
  ```
  [
  [1,2,3],
  [4,5,6]
  ]
  [
  [10,2,31],
  [43,52,62]
  ]
  ret: 左连接
  [
  [1,2,3,10,2,31],
  [4,5,6,nan,nan,nan]
  ]

  ret: 内连接
  [
  [1,2,3,10,2,31]
  ]

  ret: 外连接
  [
  [1,2,3,10,2,31]
  [4,5,6，nan,nan,nan]
  [nan,nan,nan,43,52,62]
  ]

  ret: 右连接
  [
  [1,2,3,10,2,31]
  [nan,nan,nan,43,52,62]
  ]
  ```

#### 数据的分组和聚合
  - groupby(by="").count()

  - groupby(by=["",""]).count() --->返回复合索引的df

  - 可迭代

#### 索引的相关知识点
  - df.index
  - df.index = []
  - df.set_index(“a”) #把某一列作为索引
  - df.set_index([“a”,"b"]) #把某几列作为索引

  - series
    - `s1["a"]["b"]`
    - `s1["a","b"]`

  - DataFrame
    - `df.loc["a"].loc["b"]`

  - 从内层开始选择
    - df.swaplevel()
