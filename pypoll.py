# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on the popular vote

#Assign a variable for thr file to load and the path
# ADD OUR DEPENDENCIES
import csv
import os
#ASSIGN A VARIABLE TO LOAD A FILE FROM A PATH
file_to_load = 'c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/Resources/election_results.csv'
#ASSIGN A VARIABLE TO SAVE THE FILE TO A PATH
file_to_save = os.path.join('c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/analysis/election_analysis.txt')   
#iNITIALIZE A TOTAL VOTE COUNTER
total_votes=0

#declaring list for the candidate options
candidate_options=[]

#CREATE A DICTIONARY 
candidate_votes={}
#CREATE VARIABLES
winning_candidate=""
winning_count=0
winning_percentage=0
#OPEN THE ELECTION RESULTS AND READ THE FILE
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

#READ THE HEADER ROW    
    headers=next(file_reader)

#PRINT EACH ROW IN THE CSV FILE
    for row in file_reader:
        #ADD TO THE TOTAL VOTE COUNT
        total_votes +=1

#PRINT THE CANDIDATE NAME FROM EACH ROW
        candidate_name=row[2]
#IF THE CANDIDATE DOES NOT MATCH ANY EXISTING CANDIDATE
        if candidate_name not in candidate_options:
#ADD IT TO THE LIST OF CANDIDATES
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1

for candidate_name in candidate_votes:
    votes=candidate_votes[candidate_name]
    vote_percentage=float(votes)/float(total_votes)*100
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if(votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
winning_candidate_summary=(f"---------------------------\n"
                           f"Winner: {winning_candidate}\n"
                           f"Winning Vote Count: {winning_count:,}\n"
                           f"Winning Percentage: {winning_percentage:.1f}%\n"
                           f"--------------------------\n")
print(winning_candidate_summary)






