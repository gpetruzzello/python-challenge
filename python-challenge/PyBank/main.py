import os
import csv

bank_csv = os.path.join('budget_data.csv')

with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    column_header = next(csvreader)

    pnl = []
    change = []

    for line in csvreader:
         
       pnl.append([line[0],int(line[1])])

    total = 0

    for i in range(len(pnl)-1):
        total += pnl[i][1]

        change.append(pnl[i+1][1] - pnl[i][1])

       
        avgChange = sum(change) / len(pnl)

maxChange = max(change)
minChange = min(change)

maxChange_index = change.index(maxChange) + 1
minChange_index = change.index(minChange) + 1

maxMonth = pnl[maxChange_index][0]
minMonth = pnl[minChange_index][0]


print ("Financial Analysis")
print ("----------------------------")
print("Total Months:", len(pnl))
print("Total: $", total)
print("Average Change: $", avgChange)
print("Greatest Increase in Profits:", maxMonth,"$", maxChange)
print("Greatest decrease in Profits:", minMonth,"$", minChange)

text = (f"Financial Analysis\n"
       f"----------------------------\n"
       f"Total Months:{len(pnl)}\n"
       f"Total:${total}\n"
       f"Average Change:{ avgChange}\n"
       f"Greatest Increase in Profits:{maxMonth, maxChange}\n"
       f"Greatest Decrease in Profits:{minMonth, minChange}\n"
   )
with open('summary.txt', "w") as txt_file:
 txt_file.write(text)