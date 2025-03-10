"""
demo12_attrs.py  属性
"""
import numpy as np

data = np.array([[1+1j, 2+4j, 3+7j], 
                 [4+2j, 5+5j, 6+8j], 
                 [7+3j, 8+6j, 9+9j]])

print(data.shape)
print(data.dtype)
print(data.ndim)
print(data.itemsize)
print(data.nbytes)
print(data.real)
print(data.imag)
print(data.T)
a = [x for x in data.flat]
print(a)


