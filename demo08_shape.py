"""
demo08_shape.py 维度操作
"""
import numpy as np

ary = np.arange(1, 19)
print(ary, ary.shape)

# 修改原始数组的维度
ary.shape = (2, 9)
print(ary, ary.shape)
ary.resize(2, 3, 3)
print(ary, ary.shape)

# 视图变维
ary2 = ary.reshape(3, 6)
print(ary2, ary2.shape)
ary[0][0][0] = 999
print(ary2, ary2.shape)
ary3 = ary.ravel()
print(ary3, ary3.shape)

# 复制变维
ary4 = ary.flatten()
print(ary4, ary4.shape)
ary[0][0][0] = 1000
print(ary4, ary4.shape)

