# The total number of months included in the dataset-
# The net total amount of "Profit/Losses" over the entire period-
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


import os

import csv

# path to csv file
csvpath = os.path.join("Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# print(csvpath)
# create variables
total_months = 0
total_amount = 0
changes = 0 
lowest_month = 0
highest_month = 0

# any list 
profit_change = []
total_months_profits = []
total_profit = []
# read file
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)


    for row in reader:
        profit_losses = float(row[1])
    #    total months 
        total_months = total_months + 1
# total of profits and losses
        total_amount = round(total_amount + profit_losses)
 
        
#  print(total_months)
# print(f'${total_amount}')
   
        

# i want the average change


# max and min function 
# greatest increase
# i need a month and an amount
# highest_month = max(profit_change)

# greatest decrease
# lowest_month = min(profit_change)


print("Financial Analysis")
print("----------------------")
print(f'Total Months : {total_months}')
print(f'Total: ${total_amount}')
print("Average Change: $")
print("Greatest Increase in Profits:")
print("Greatest Decrease in Profits:")

output_file = os.path.join("budget_data.txt")
with open(output_file, "w", newline = '') as datafile:

    datafile.write("Financial Analysis\n")
    datafile.write("----------------------\n")
    datafile.write(f'Total Months : {total_months}\n')
    datafile.write(f'Total: ${total_amount}\n')
    datafile.write('Average Change: $\n')
    datafile.write('Greatest Increase in Profits:\n')
    datafile.write('Greatest Decrease in Profits: \n')