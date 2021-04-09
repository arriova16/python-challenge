import os 
import csv


# path to csv file
input_file = os.path.join("Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")


# create global variables
vote_total = 0
candidates_list = []
candidates_votes = []


# read file
with open(input_file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:
# read in total votes
        vote_total = vote_total +1 
# read in candidate name 
        candidates_name = (row[2])
# list of candidates and adding to it
        if candidates_name in candidates_list :
            candidate_index = candidates_list.index(candidates_name)
            candidates_votes[candidate_index] = candidates_votes[candidate_index] +1
        else:
            candidates_list.append(candidates_name)
            candidates_votes.append(1)

# testing code           
# print(f'{vote_total}')
# print(f'{candidates_list}')

# i want to get percentage of votes for each 
# total number of votes for each candidate
# winner of the election
percent_votes = []
vote_per_candidate = candidates_votes[0]
max_votes = 0

# loop through the candidates and get the percent
for x in range(len(candidates_list)):
    percent = (candidates_votes[x]/vote_total * 100)
    percent_votes.append(percent)

# winner within the candidate list
    if candidates_votes[x] > vote_per_candidate:
        vote_per_candidate = candidates_votes[x]
        max_votes = x
        

winner = candidates_list[max_votes]  
# testing
# print(f'{vote_per_candidate}')
# print(f'{winner}')
# print(f'{candidates_votes}')
# line break


# print(output_file)
# output_file = os.path.join("analysis", "election_analysis.txt")
# with open(output_file, "w", newline = '') as datafile:
#     writer = csv.writer(datafile)

# i need to get a list of votes per candidates and the percent of votes
# needs to loop

print("Election Results")
print("------------------------------------------")
print(f"Total Votes:{vote_total}")
print("------------------------------------------")
for x in range(len(candidates_list)):
    print(f'{candidates_list[x]} : {percent_votes[x]} {candidates_votes[x]}')
print("------------------------------------------")
print(f'Election winner: {winner}')
print("------------------------------------------")