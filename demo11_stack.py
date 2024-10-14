"""
demo11_stack.py 组合操作
"""
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

print(a)
print(b)

print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(np.dstack((a, b)))

c = np.vstack((a, b))   # (4, 3)
a, b = np.vsplit(c, 2)
print(c)
print(a)
print(b)

c = np.hstack((a, b)) # (2, 6)
a, b = np.hsplit(c, 2)
print(c)
print(a)
print(b)

c = np.dstack((a, b))
a, b = np.dsplit(c, 2)
print(c)
print(a)
print(b)

a = a.reshape(2, 3)
b = b.reshape(2, 3)
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=1))


a = np.arange(1, 9)
b = np.arange(9, 17)
print(np.row_stack((a, b)))
print(np.column_stack((a, b)))








