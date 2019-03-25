#import dependency
import os
import csv

#set file path
csvpath = "03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv"

#empty list to iterate through rows
months_list = []
profit_list = []
revenue = []

# #open csv
# matt is an object that python is container all the information inside the csv into
# julia is actually reading the line by line content inside matt (the container)
with open(csvpath, newline='') as matt:

    julia = csv.reader(matt, delimiter=',')
# #skip header
    header = next(julia)

    for row in julia:
          thismonthrevenue = int(row[1])
          months_list.append(row[0])
          profit_list.append(int(row[1]))
          revenue.append(int(row[1]))

number_of_months = len(months_list)
totalprofit= sum(profit_list)
total_revenue = len(revenue)

print("Financial Analysis")
print("-------------------")
print(number_of_months)
print(totalprofit)
print(total_revenue)


