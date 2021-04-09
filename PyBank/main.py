# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
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

# any list or dict 


# read file
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)


    for row in reader:
        total_months = total_months + 1
print(total_months)


# output_file = os.path.join("budget_data.txt")
# with open(output_file, "w", newline = '') as datafile:

# print("Financial Analysis")
# print("----------------------")
# print("Total Months :" + total_months)
# print("Total: " + total_amount)
# print("Average Change:" + changes)
# print("Greatest Increase in Profits:"_____ )
# print("Greatest Decrease in Profits:"_____ )