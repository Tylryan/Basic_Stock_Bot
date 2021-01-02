import pandas as pd
import random
import csv

content = []

with open('purchase_record.csv','r') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for i in csv_reader:
        content.append(i)

stock_price = random.randint(50, 100)
stock_held = int(content[-1][2])
print(f"You currently have {stock_held} stock(s)")
print(f'Current Stock Price: ${stock_price}\n'
      f'------------------------------------')
if stock_price <= 60:
    if stock_held == 0:
        stock_held +=1
        content.append([stock_price,'Bought',stock_held])
        print(f"You just bought this stock for ${stock_price} ")

        last_action_price = content[2:][-2][0]
        last_action = content[2:][2][1]

        if last_action == 'Sold':
            last_action = last_action *-1
        else:
            last_action = last_action

        percent_return = round((stock_price / int(last_action_price) - 1) * 100, 2)
        print(f" Your return on that was {percent_return}%")
    else:
        print('You already have stock.')

if stock_price >70:
    if stock_held == 1:
        stock_held -= 1
        content.append([stock_price,'Sold', stock_held])
        print(f"You just sold this stock for ${stock_price}")

        last_action_price = content[2:][-2][0]
        last_action = content[2:][2][1]

        if last_action == 'Sold':
            last_action = last_action *-1
        else:
            last_action = last_action

        percent_return = round((stock_price / int(last_action_price) - 1) * 100, 2)
        print(f" Your return on that was {percent_return}%")
    else:
        print('You do not have stock to sell')

# with open('purchase_record.csv','w', newline= '') as file:
#     csv_writer = csv.writer(file, delimiter = ',')
#     for i in content:
#         csv_writer.writerow(i)
