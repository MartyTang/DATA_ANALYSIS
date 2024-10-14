"""
demo05_dtype.py 数据类型
"""
import numpy as np

ary = np.array([1, 2, 3, 4], dtype='float32')
print(ary, ary.dtype)

ary = ary.astype('str')
print(ary, ary.dtype)