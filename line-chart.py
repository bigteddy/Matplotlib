# import matplotlib.pyplot as plt

"""
    (1, 4), (2, 5), (3, 6)
"""
# plt.plot([1, 2, 3],[4, 5, 6])
# plt.show()

'''
    two groups:
    1st: (1, 2), (2, 4), (3, 6)
    2nd: (1, 1), (2, 2), (3, 3)
'''

# plt.plot([1, 2, 3], [[2,1],[4,2],[6,3]], label=['1st', '2nd'])
# plt.legend()
# plt.xlabel('Time')
# plt.ylabel('speed')
# plt.show()

import matplotlib.pyplot as plt
import csv
file = open('./Matplotlib/line-chart-data.csv')
reader = csv.reader(file)
header = next(reader)
print('title', header)

x = []
y = []
for row in reader:
    print(f"line: {row}")
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2]), int(row[3])])
    
plt.plot(x, y, label=header[1:4])  
plt.legend()
plt.xlabel(header[0])
plt.ylabel('Price')
plt.show()
