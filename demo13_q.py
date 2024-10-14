import numpy as np


def loadtxt():   
    """
    加载CustomerSurvival.csv
    """
    header = []
    data = []
    with open('CustomerSurvival.csv', 'r') as f:
        for index, line in enumerate(f.readlines()):
            if index == 0:
                header = line[:-1].split(',')
            else:
                data.append(tuple(line[:-1].split(',')))
        result = np.array(data, dtype={'names':header, 'formats':['f8', 'f8', 'f8', 'f8', 'f8', 'f8']})
    return result

data = loadtxt()
print(data.shape, data[0])

# 统计额外剩余时长，额外剩余流量，使用月份三个字段的 最小值，最大值，平均值，做出业务分析。
print('-' * 100)
extra_time_col = data['extra_time']
print('[extra_time] min:', min(extra_time_col), ' max:', max(extra_time_col), 'mean:', sum(extra_time_col) / len(extra_time_col))
extra_flow_col = data['extra_flow']
print('[extra_flow] min:', min(extra_flow_col), ' max:', max(extra_flow_col), 'mean:', sum(extra_flow_col) / len(extra_flow_col))
use_month_col = data['use_month']
print('[use_month] min:', min(use_month_col), ' max:', max(use_month_col), 'mean:', sum(use_month_col) / len(use_month_col))


# 统计所有有额外剩余通话时长的人数占总人数的比例。 统计所有有额外剩余流量的人数占总人数的比例。
print('-' * 100)
print(data[data['extra_time'] > 0].size / data.size)
print(data[data['extra_flow'] > 0].size / data.size)

# 统计每一类套餐的人数与总人数的占比并输出。
print('-' * 100)
types = set(data['pack_type'])
for t in types:
    print(t, ':', len(data[data['pack_type']==t]) / len(data))
