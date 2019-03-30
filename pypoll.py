#import dependency
import os
import csv

#set variables

total_vote = 0
khan_vote = 0
li_vote = 0
correy_vote = 0
tooley_vote = 0

csvpath = ("Resources/election_data.csv")

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

#iterate through each row in csv

    for row in csvreader:
        total_vote +=1
        if row[2]=="Khan":
            khan_vote +=1
        elif row[2]=="Correy":
            correy_vote +=1
        elif row[2]=="Li":
            li_vote +=1
        elif row[2]=="O'Tooley":
            tooley_vote +=1

percent_khan = (khan_vote) / (total_vote)

num_khan = int(percent_khan)

num = "{:.1%}".format[num_kahn]

print(num)


print("Election Results")
print("----------------------------")
print("Total Vote =", total_vote)
print("Khan", khan_vote)
print("Li", li_vote)
print("Correy", correy_vote)
print("Tooley", tooley_vote)

print("----------------------------")