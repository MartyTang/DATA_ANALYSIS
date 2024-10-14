"""
demo10_mask.py 掩码
"""
import numpy as np

a = np.arange(1, 101)
print(a[a%3==0])
a[a%3==0] = 999
print(a)

names = np.array(['Mi', 'Apple', 'Huawei', 'Oppo', 'Vivo'])
rank = [0, 3, 4, 2, 1, 3, 2, 1]
print(names[rank])



