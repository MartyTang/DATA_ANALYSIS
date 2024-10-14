"""
demo02_numpy.py  numpy演示
"""
import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))

print(ary * 2)
print(ary + ary)

print(ary > 2)
print(ary * ary)

ary2 = np.array([1, 2, 3, 4, 5])
print(ary * ary2)
