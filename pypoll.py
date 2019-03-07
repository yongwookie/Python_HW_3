import os
import csv

#set variables

total_vote = []
khan_vote = []
li_vote = []
correy_vote = []
tooley_vote =[]


csvpath = ("03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

#iterate through each row in csv

for row in csvreader:
    total_vote +=1

    if row[2]=="Khan":
        khan_vote +=1
    elif row[2]=="Correy"
        correy_vote +=1
    elif row[2]=="Li":
        li_vote +=1
    elif row[2]=="O'Tooley":
        tooley_vote +=1
        

print(total_vote)