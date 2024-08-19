import matplotlib.pyplot as plt

'''
    x axis:  
    x = [3, 4, 1]
    height = [8, 5, 2]
'''
# plt.bar([3, 4, 1], [8, 5, 2])
# plt.show()

'''
    x axis:  
    x = ['p', 'a', 't']
    height = [8, 10, 16]
'''
# plt.bar(['P', 'A', 'T'], [8, 10, 16], width=0.3, color='green')

# plt.xlabel('Compnay Name')
# plt.ylabel('Revenue in 2030')
# plt.show()

import csv
file = open('./Matplotlib/bar-chart-data.csv')
reader = csv.reader(file)
header = next(reader)
# print(reader)

x = []
height = []
for row in reader:
    x.append(row[0])
    height.append(int(row[1]))

print(x)
print(height)

plt.bar(x, height, width=0.6, color='green')
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.legend()
plt.show()