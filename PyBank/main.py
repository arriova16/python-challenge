import os

import csv

# path to csv file
csvpath = os.path.join("Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data")

print(csvpath)


# read file
with open(csvpath,'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))