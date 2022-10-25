import csv
import os
from telnetlib import theNULL

# declare paths
bankcsvpath = os.path.join("Week 3","Instructions","PyBank","Resources","budget_data.csv")
#Week 3\Instructions\PyBank\Resources\budget_data.csv
pollcsvpath = os.path.join("Week 3","Instructions","PyPoll","Resources","election_data.csv")

# declare bank variables
numMonths = 0
netTotal = 0
greatestIncrease = 0
greatestIncreaseMo = ""
greatestDecrease = 0
greatestDecreaseMo = ""
oldValue = 0
beginValue = 0
endValue = 0
with open(bankcsvpath, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        numMonths = numMonths + 1
        netTotal = netTotal + int(row[1])
        if numMonths == 1:
            beginValue = int(row[1])
        else:
            endValue = int(row[1])
        if (int(row[1])-oldValue) > greatestIncrease:
            greatestIncrease = (int(row[1])-oldValue)
            greatestIncreaseMo = row[0]
        elif (int(row[1])-oldValue) < greatestDecrease:
            greatestDecrease = (int(row[1])-oldValue)
            greatestDecreaseMo = row[0]
        oldValue = int(row[1])
    
    print("Financial Analysis \n ----------------------------")
    print(f"Total Months: {numMonths}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${round((endValue-beginValue)/(numMonths-1),2)}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMo} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMo} (${greatestDecrease})")
    print("\n\n")

# declare poll variables
pollAgg = {}
tempAgg =0
totalVotes = 0
winnerTally = 0
winner = ''
with open(pollcsvpath, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#     #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        totalVotes = totalVotes + 1
        if row[2] in pollAgg:
            tempAgg = int(pollAgg[row[2]]) + 1
            pollAgg.update({row[2]: tempAgg})
        else:
            pollAgg[row[2]] = 1
    print(f"Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------")
    for votes in pollAgg:
        print(f"{votes}: {round((pollAgg[votes]/totalVotes)*100,3)}% ({pollAgg[votes]})")
    for votes in pollAgg:
        if pollAgg[votes] > winnerTally:
            winnerTally = pollAgg[votes]
            winner = votes
    print(f"-------------------------\nWinner: {winner}\n-------------------------")

