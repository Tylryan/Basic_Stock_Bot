import pandas as pd
import random
import csv

content = []

with open('purchase_record.csv','r') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for i in csv_reader:
        content.append(i)

stock_price = random.randint(50, 100)
stock_held_sup = 0
stock_held = int(content[-1][2])
print(stock_held)
print(stock_price)
if stock_price >= 70:
    if stock_held == 0:
        stock_held +=1
        content.append([stock_price,'Bought',stock_held])
        print('Bought')
    else:
        print('You already have stock.')

if stock_price <70:
    if stock_held == 1:
        stock_held -= 1
        content.append([stock_price,'Sold', stock_held])
        print('Sold')
    else:
        print('You do not have stock to sell')

with open('purchase_record.csv','w', newline= '') as file:
    csv_writer = csv.writer(file, delimiter = ',')
    for i in content:
        csv_writer.writerow(i)
