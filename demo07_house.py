"""
demo07_hourse.py 房价数据
"""
import numpy as np

data = [('宝星华庭一层带花园', '4室1厅', 298.79, 2598, 86951), 
        ('绿地花园', '3室2厅', 154.62, 1000, 64675), 
        ('沁园公寓', '3室2厅', 177.36, 1200, 67659)]

ary = np.array(data, dtype={'names':['title', 'houseType', 'square', 'totalPrice', 'unitPrice'], 
                      'formats':['20U', '10U', 'f8', 'f8', 'f8']})

print(ary)
print(ary['totalPrice'])
