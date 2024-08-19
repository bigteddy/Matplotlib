import matplotlib.pyplot as plt

'''
    (2, 4), (4, 3), (3, 6)
'''
# plt.scatter([2, 4, 3], [4, 3, 6], c='red', s=30)
# plt.scatter([2, 4, 3], [4, 3, 6], c='#888888', s=100)
# plt.show()

'''
    (2, 4), (4, 3), (3, 6)
    (1, 2), (3, 5), (4, 4)
'''

# plt.scatter([2, 4, 3], [4, 3, 6], label= 's1', s=30)
# plt.scatter([1, 3, 4], [2, 5, 4], label= 's2', s=30)
# plt.legend()
# plt.show()

import csv
file = open('./Matplotlib/scatter-chart-data.csv')
reader = csv.reader(file)
next(reader)

data = {
    "Boy": {"x":[], "y":[]},
    "Girl": {"x":[], "y":[]}
}

for row in reader:
    # print(row)
    gender=row[0]
    data[gender]['x'].append(int(row[1]))
    data[gender]['y'].append(int(row[2]))
    
plt.scatter(data['Boy']['x'], data['Boy']['y'], label='Boys')
plt.scatter(data['Girl']['x'], data['Girl']['y'], label='Girls')
plt.legend()
plt.show()
