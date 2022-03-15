# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on the popular vote

#Assign a variable for thr file to load and the path
file_to_load = 'c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)
import csv
import os

file_to_save = os.path.join('c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/analysis/election_analysis.txt')
with open(file_to_save,"w") as txt_file:
   
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
    
import csv
import os   
file_to_load = 'c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/Resources/election_results.csv'
file_to_save = os.path.join('c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/analysis/election_analysis.txt')   
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    for row in file_reader:
        print(row)
import csv
import os   
file_to_load = 'c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/Resources/election_results.csv'
file_to_save = os.path.join('c:/Users/SUKANYA GHOSH/Desktop/Election_Analysis_Practice/analysis/election_analysis.txt')   
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)


