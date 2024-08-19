import matplotlib.pyplot as plt

# plt.rc()
# plt.pie([10,  15,  25], ;=['10', '15', '25'], labeldistance=0.5)
# plt.legend()
# plt.title('Percentage Show')
# plt.show()


x = [10,  15,  25]
total = sum(x)
labelss=[str(100*data/total) + '%' for data in x]
# plt.pie(x, labels=[str(100*x[0]/total)+'%', str(100*x[1]/total)+'%', str(100*x[2]/total)+'%'],
#                    labeldistance=0.5)
plt.pie(x, labels=labelss, labeldistance=0.5)
plt.legend()
plt.title('Percentage Show')
plt.show()

# import csv
# file = open('./Matplotlib/pie-chart-data.csv')
# reader = csv.reader(file)
# next(reader)

# x =[]
# labels = []
# for row in reader:
#     labels.append(row[0])
#     x.append(int(row[1]))
# plt.pie(x, labels=labels, labeldistance=1.1)
# plt.legend()
# plt.title('Market analyst for the Browser')
# plt.show()

