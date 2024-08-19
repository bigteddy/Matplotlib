import matplotlib.pyplot as plt

'''
    Date: Price
    11/01   open 95, close 80, hight 100, low 75
    11/02   open 82, close 75, hight 83, low 62
    11/03   open 73, close 85, hight 90, low 70
'''

# plt.bar("11/01", 15, bottom=80, color='red', width=0.5)
# plt.bar("11/01", 25, bottom=75, color='red', width=0.1)
# plt.bar("11/02", 7, bottom=75, color='red', width=0.5)
# plt.bar("11/02", 18, bottom=65, color='red', width=0.1)
# plt.bar("11/03", 12, bottom=73, color='green', width=0.5)
# plt.bar("11/03", 20, bottom=70, color='green', width=0.1)
# plt.show()


import csv
file = open('./Matplotlib/candlestick-chart-data.csv')
reader = csv.reader(file)
header = next(reader)
print(header)

for row in reader:
    date = row[0]
    open_price = int(row[1])
    close_price = int(row[2])
    highest = int(row[3])
    lowest = int(row[4])
    
    color = 'red'
    if close_price > open_price:
        color = 'green'
    
    plt.bar(
        date,
        abs(open_price - close_price),
        bottom = min(open_price, close_price),
        color = color, width = 0.5
    )
    
    plt.bar(
        date, 
        highest - lowest, 
        bottom = lowest, 
        color = color, width = 0.1)
    
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('TSLA Stock in November')
plt.show()
    