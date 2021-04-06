import os 
import csv



input_file = os.path.join("Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
# print(input_file)
output_file = os.path.join("analysis", "election_analysis.txt")

# create global variables
vote_total = 0
percent_votes = 0
winner_won = 0
name = 0
vote = 0
# dict to store candidates name
candidates = {}
candidates_votes = {}





# outter loop
with open(input_file) as election_data:
    reader = csv.reader(election_data, delimiter = ",")
    header = next(reader)
    
    for row in reader:
# read in total votes
        vote_total = vote_total +1 
# read in candidate name 
        candidate_name = (row[2])
# adding in vote count per candidate?
        if candidate_name in candidates :
            candidate_votes = candidate_votes + 1
        print(f"Candidate votes: {candidate_votes}")


        # remaing loop
   

# line break

# i want to get the names of every candidate
    
def candidates_votes(candidate_data):
    name = str(candidate_data[2])
    votes = int(candidate_data)
    
#     if name == name :
#         votes = vote + 1
#     print(f"candidate names:{votes}")
#  percent of votes   
percent_votes_candidate = (won_vote/ vote_total)

# total votes each candidate won 
candidate_votes = 

# print("Election Results")
# print("------------------------------------------")
 # print(f"Total Votes:{vote_total}")
#  print("------------------------------------------")