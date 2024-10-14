"""
demo06_dtype.py 复合数据类型
"""
import numpy as np

data = [('zs', [90, 98, 96], 15), 
        ('ls', [91, 92, 92], 16), 
        ('ww', [92, 95, 94], 17)]
    
ary = np.array(data, dtype='2U, 3i4, i4')
print(ary, ary[2][2])

ary = np.array(data, dtype={'names':['name', 'scores', 'age'], 'formats':['2str', '3int32', 'int32']})
print(ary, ary[2]['age'])

ary = np.array(data, dtype=[('name', 'str', 2), ('scores', 'int32', 3), ('age', 'int32', 1)])
print(ary, ary[0]['scores'])

print(ary['age'])

# 使用ndarray保存日期数据类型
dates = np.array(['2011', '2011-02', '2011-03-01', '2011-04-01 10:10:10'])
ndates = dates.astype('M8[D]')
print(ndates, ndates.dtype)
print(ndates[-1] - ndates[0])





