# coding=utf-8 
# Time : 2018/11/21 21:54 
# Author : achjiang
# File : test1_count.py
import numpy as np
import random


t1 = np.array([1,2,3])
print(t1)
print(type(t1))
"""打印结果：
[1 2 3]
<class 'numpy.ndarray'>
"""


t2 = np.array(range(10))
print(t2)
print(type(t2))
"""打印结果：
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
"""


t3 = np.arange(1,12,2)
print(t3)
print(type(t3))
"""打印结果：
[ 1  3  5  7  9 11]
<class 'numpy.ndarray'>
"""

# 使用dtype设置数量类型
t4 = np.array([1,2,3,5,2], dtype=bool) # dtype数值类型定义，有int/float等
print(t4)
print(type(t4), t4.dtype)   # t4.dtype表示t4的数值类型
"""打印结果：
[ True  True  True  True  True]
<class 'numpy.ndarray'> bool
"""


# 使用astype方法调整数据类型
t5 = t4.astype('int8') # astype是调整数据类型
print(t5)
print(type(t5), t5.dtype)
"""打印结果：
[1 1 1 1 1]
<class 'numpy.ndarray'> int8
"""

# numpy中的小数处理
t6 = np.array([random.random() for i in range(10)])
print(t6)
print(type(t6), t6.dtype)
"""打印结果：
[0.34412697 0.95924103 0.1855649  0.62660822 0.75105713 0.67238014
 0.38100326 0.80884152 0.74501869 0.81650096]
<class 'numpy.ndarray'> float64
"""

t7 = np.round(t6, 2)
print(t7)
print(type(t7), t7.dtype)
"""打印结果：
[0.34 0.96 0.19 0.63 0.75 0.67 0.38 0.81 0.75 0.82]
<class 'numpy.ndarray'> float64
"""
