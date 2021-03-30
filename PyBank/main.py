import os

import csv

csvpath = os.path.join("..",'Resources', 'Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

print(csvpath)

with open(csvpath,'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))