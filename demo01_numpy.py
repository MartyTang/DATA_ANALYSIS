"""
demo01_numpy.py  numpy演示
"""
import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))

for i in ary:
    print(i)

print(ary[0], ary[1:3])