import os
import csv
import operator


csvpath = os.path.join('election_data.csv')


with open(csvpath, newline='') as csvfile:
   
   csvreader = csv.reader(csvfile, delimiter=',')
   
   # Read the header
   csv_header = next(csvreader)
   
   i=0

   candidate_dict={}

   # Read each row of data after the header
   for row in csvreader:
       i = i+1
       row_candidate = row[2]
       if row_candidate in candidate_dict:
           candidate_dict[row_candidate] += 1
       else:
           candidate_dict[row_candidate]= 1
      
print ("Election Results")
print ("----------------------------")

total_votes=i
print("Total Votes:",total_votes)
print ("----------------------------")

for key in candidate_dict.keys() :
  
   print(key, ": ", candidate_dict[key]/total_votes*100, "%(", candidate_dict[key],")")

print("Winner is:")

print(max(candidate_dict, key=candidate_dict.get))


summary = []
for key in candidate_dict.keys() :
 summary.append("{} : {} % ({})".format(key, candidate_dict[key]/total_votes*100, candidate_dict[key]))
text = (f"Election Results\n"
      f"--------------------\n"
      f"Total Votes: {total_votes}\n"
      f"--------------------\n"
      f"{summary[0]}\n"
      f"{summary[1]}\n"
      f"{summary[2]}\n"
      f"{summary[3]}\n"
      f"--------------------\n"
      f"Winner is : {max(candidate_dict, key=candidate_dict.get)}\n"
      f"---------------------\n")
with open('summary.txt', "w") as txt_file:
  txt_file.write(text)