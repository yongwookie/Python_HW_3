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
    elif row[2]=="Correy":
        correy_vote +=1
    elif row[2]=="Li":
        li_vote +=1
    elif row[2]=="O'Tooley":
        tooley_vote +=1
        

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")
