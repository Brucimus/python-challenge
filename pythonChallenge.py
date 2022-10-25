import csv
import os

# declare paths for reading and writing
bankcsvpath = os.path.join("Week 3","Instructions","python-challenge","PyBank","Resources","budget_data.csv")
banktextpath = os.path.join("Week 3","Instructions","python-challenge","PyBank","Analysis","budget_data.txt")
pollcsvpath = os.path.join("Week 3","Instructions","python-challenge","PyPoll","Resources","election_data.csv")
polltextpath = os.path.join("Week 3","Instructions","python-challenge","PyPoll","Analysis","election_data.txt")

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

#open bank csv file
with open(bankcsvpath, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #iterate throw rows to gather data
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
    
    #write into txt file
    with open(banktextpath,'w') as f:
        f.write(f"Financial Analysis \n----------------------------\n")
        f.write(f"Total Months: {numMonths}\n")
        f.write(f"Total: ${netTotal}\n")
        f.write(f"Average Change: ${round((endValue-beginValue)/(numMonths-1),2)}\n")
        f.write(f"Greatest Increase in Profits: {greatestIncreaseMo} (${greatestIncrease})\n")
        f.write(f"Greatest Decrease in Profits: {greatestDecreaseMo} (${greatestDecrease})\n")

# declare poll variables
pollAgg = {}
tempAgg =0
totalVotes = 0
winnerTally = 0
winner = ''

#open polls csv file
with open(pollcsvpath, newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #iterate throw rows to gather data
    for row in csvreader:
        totalVotes = totalVotes + 1
        if row[2] in pollAgg:
            tempAgg = int(pollAgg[row[2]]) + 1
            pollAgg.update({row[2]: tempAgg})
        else:
            pollAgg[row[2]] = 1

    #write into txt file
    with open(polltextpath,'w') as f:
        f.write(f"Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------\n")
        for votes in pollAgg:
            f.write(f"{votes}: {round((pollAgg[votes]/totalVotes)*100,3)}% ({pollAgg[votes]})\n")
        for votes in pollAgg:
            if pollAgg[votes] > winnerTally:
                winnerTally = pollAgg[votes]
                winner = votes
        f.write(f"-------------------------\nWinner: {winner}\n-------------------------\n")

