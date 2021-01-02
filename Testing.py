import csv
import random
from Bot import content
import statistics

with open('purchase_record.csv','r') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for i in csv_reader:
        content.append(i)
stock_price = random.randint(50,100)
last_action_price = content[2:][-2][0]
last_action = content[2:][2][1]

if last_action == 'Sold':
    last_action = -(last_action)

percent_return = round((stock_price / int(last_action_price) - 1) * 100,2)