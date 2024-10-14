"""
demo03_ndarray.py  numpy演示
"""
import numpy as np

ary = np.array([[1, 3, 5], [2, 4, 6]])
print(ary)

ary2 = np.arange(0, 10, 2)
print(ary2)

ary3 = np.ones(10)
print(ary3)

ary3 = np.zeros(10, dtype='int32')
print(ary3)

ary4 = np.ones_like(ary)
print(ary4)

ary5 = np.zeros_like(ary)
print(ary5)

print(np.ones(5) / 5)

