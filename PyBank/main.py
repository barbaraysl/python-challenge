#Read File
import os
import csv

# csvpath=os.path.join('budget_data.csv')
# with open(csvpath,newline='') as csvfile:
#     csvreader=csv.reader(csvfile,delimiter=',')
#     print(csvreader)
#     csv_header=next(csvreader)
#     print(f"CSV Header:{csv_header}")
#     for row in csvreader:
#         print(row)


import pandas as pd
py_bank=pd.read_csv('budget_data.csv')
    # print(py_bank)

print("Financial Analysis")
print("----------------------------")
count=len(py_bank['Date'])
print("Total Months:"+str(count))

#Calculate Sum
total=py_bank['Profit/Losses'].sum()
print("Total:$"+str(total))

#Calculate Mean
mean=py_bank['Profit/Losses'].mean()
print("Average Change:$"+str(mean))

#Greatest Increase
great_increase=py_bank['Profit/Losses'].max()
#Find Relevant Month
max_date=py_bank.loc[py_bank['Profit/Losses']==great_increase,'Date']
print("Greatest Increase in Profits: "+ max_date+": $"+str(great_increase))

#Greatest Decrease
great_decrease=py_bank['Profit/Losses'].min()
min_date=py_bank.loc[py_bank['Profit/Losses']==great_decrease,'Date']
print("Greatest Decrease in Profits: "+ min_date+": $"+str(great_decrease))