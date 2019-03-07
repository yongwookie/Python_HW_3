import os
import csv


csvpath = ("03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(row[1])

number_of_months = len(total_months)

total_revenue = 0
i = 0

for i in range(number_of_months):
    total_revenue = total_revenue + int(total_profit[i])


#When calculating the average revenue change the intervals is one less than total months
average_change_revenue = round(change_revenue/(months-1),2)


print("Financial Analysis")
print("--------------")
print(number_of_months)
print(total_revenue)
print("Average Change + {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}" )