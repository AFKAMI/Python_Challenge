import os
import csv
PyBank_csv = os.path.join('Resources','election_data.csv')

votes = []
Candidate_names = [] 
cand_1 = "Charles Casper Stockham"
cand_2 = "Diana DeGette"
cand_3 = "Raymon Anthony Doane"
cand_1_list = []
cand_2_list = []
cand_3_list = []

#import data
with open(PyBank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    for row in csv_reader:
     # calculate total votes
     votes.append(row[0])

      # how to remove duplication from a list

     if (row[2]) not in Candidate_names: Candidate_names.append(row[2]) 
   
     
    #calculate the len of each candidate's votes to add them sepratly into 3 lists
     
     if (row[2]) == cand_1 : 
        cand_1_list.append(row[2])
        
     elif (row[2]) == cand_2 : 
        cand_2_list.append(row[2])
     elif (row[2]) == cand_3 : 
        cand_3_list.append(row[2])

total_votes= len(votes)

total_cand_1 = len(cand_1_list)

total_cand_2 = len(cand_2_list)

total_cand_3 = len(cand_3_list)

#calculate vote percentage
vote_percentage_1 = round(total_cand_1/ total_votes,3)*100
vote_percentage_2 = round(total_cand_2/ total_votes,3) *100
vote_percentage_3 = round(total_cand_3/ total_votes,3) *100

# creat dictionary to find the winner based on max percentage
candidate_votes = {
   "name": [cand_1,cand_2 ,cand_3 ],
    "vote_per": [vote_percentage_1,vote_percentage_2,vote_percentage_3]
    }

winner = float(max(candidate_votes["vote_per"]))

#using for loop to calculate the index for "vote_per" to get the winner index 
i=0
for row in candidate_votes["vote_per"]:
   #print(row)
   if winner == float(row):
      II=i
   i=i+1 




output_path = os.path.join("Analysis", "result.txt")

with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
     csvwriter = csv.writer(csvfile, delimiter=',')
     csvwriter.writerow(["-----------------------------"])
     csvwriter.writerow(['Election Results'])
     csvwriter.writerow(["-----------------------------"])
     csvwriter.writerow([f' Total Votes: {total_votes}'])
     csvwriter.writerow(["-----------------------------"])
     csvwriter.writerow([f' {cand_1} : {vote_percentage_1}% {(total_cand_1)}'])
     csvwriter.writerow([f' {cand_2} : {vote_percentage_2}% {(total_cand_2)}'])
     csvwriter.writerow([f' {cand_3} : {vote_percentage_3}% {(total_cand_3)}'])
     csvwriter.writerow(["-----------------------------"])
     csvwriter.writerow([f' Winner : {candidate_votes["name"][II]}'])   
     csvwriter.writerow(["-----------------------------"])
     
