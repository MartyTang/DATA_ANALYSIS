"""
demo04_attr.py  属性基本操作
"""
import numpy as np

ary = np.arange(1, 10)
print(ary)

# shape属性
print(ary, ary.shape)
ary.shape = (3, 4)
print(ary, ary.shape)

# dtype属性
print(ary, ary.dtype)
# ary.dtype = 'float32'
# print(ary, ary.dtype)
ary = ary.astype('float32')
print(ary, ary.dtype)

# size属性
print(ary.size, len(ary))
