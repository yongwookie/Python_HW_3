#import dependency
import os
import csv

#set file path
csvpath = "03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv"

#empty list to iterate through rows
months_list = []
profit_list = []
changelist = []

previous = 0
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
        change = thismonthrevenue - previous
        previous = thismonthrevenue
        changelist.append(change)


max_value = max(changelist)
max_index = changelist.index(max_value)

min_value = min(changelist)
min_index = changelist.index(min_value)



changelist.pop(0)
average_change = sum(changelist) / len(months_list)



number_of_months = len(months_list)
totalprofit= sum(profit_list)


print("Financial Analysis")
print("-------------------  ")
print(number_of_months)
print(totalprofit)
print("max month", max_value, months_list[max_index])
print("min month", min_value, months_list[min_index])
print(average_change)
#The average of the changes in "Profit/Losses" over the entire period





# #opens the output file in r mode and prints to terminal
# with open(output_dest, 'r') as readfile:
#     print(readfile.read())
