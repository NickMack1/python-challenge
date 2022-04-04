## Module to allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set csv file location (navigate from where this .py file is saved)
Election_csv = os.path.join('PyPoll','Resources', 'election_data.csv')

Candidate_list = []
candidate_vote_count = {}


# Open file using CSV module
with open(Election_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader, None)
   
    # ForLoop: loop through each row
    for row in csvreader: 

        Candidate_list.append(str(row[2]))



for item in Candidate_list:
    candidate_vote_count[item] = candidate_vote_count.get(item, 0) + 1
new_key = "Otooley"
old_key = "O'Tooley"
candidate_vote_count[new_key] = candidate_vote_count.pop(old_key)
print(candidate_vote_count)


khan_percent = round(candidate_vote_count["Khan"]/len(Candidate_list)*100)
Correy_percent = round(candidate_vote_count["Correy"]/len(Candidate_list)*100)
Li_percent = round(candidate_vote_count["Li"]/len(Candidate_list)*100)
Otooley_percent = round(candidate_vote_count["Otooley"]/len(Candidate_list)*100)
most_votes = max(candidate_vote_count, key=candidate_vote_count.get)

print("Election Results")
print("-------------------------------------")
print(f'Total Votes: {len(Candidate_list)}')
print("-------------------------------------")
print(f'Khan: {khan_percent}% ( {candidate_vote_count["Khan"]} )')
print(f'Correy: {Correy_percent}% ( {candidate_vote_count["Correy"]} )')
print(f'Li: {Li_percent}% ( {candidate_vote_count["Li"]} )')
print(f'OTooley: {Otooley_percent}% ( {candidate_vote_count["Otooley"]} )')
print("-------------------------------------")
print(f'Winner: {most_votes}')

f = open("Election Results HW.txt", "a")
print("Election Results", file=f)
print("-------------------------------------", file=f)
print(f'Total Votes: {len(Candidate_list)}', file=f)
print("-------------------------------------", file=f)
print(f'Khan: {khan_percent}% ( {candidate_vote_count["Khan"]} )', file=f)
print(f'Correy: {Correy_percent}% ( {candidate_vote_count["Correy"]} )', file=f)
print(f'Li: {Li_percent}% ( {candidate_vote_count["Li"]} )', file=f)
print(f'OTooley: {Otooley_percent}% ( {candidate_vote_count["Otooley"]} )', file=f)
print("-------------------------------------", file=f)
print(f'Winner: {most_votes}', file=f)
f.close()