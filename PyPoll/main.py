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
    reader = csv.reader(election_data, delimiter = ",")
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

            
print(f'{vote_total}')
print(f'{candidates_list}')





        # remaing loop
   

# line break

# i want to get the names of every candidate
    
# def candidates_votes(candidate_data):
#     name = str(candidate_data[2])
#     votes = int(candidate_data)
    
# #     if name == name :
# #         votes = vote + 1
# #     print(f"candidate names:{votes}")
# #  percent of votes   
# percent_votes_candidate = (won_vote/ vote_total)

# total votes each candidate won 
# candidate_votes = 
# # print(input_file)
# output_file = os.path.join("analysis", "election_analysis.txt")

# print("Election Results")
# print("------------------------------------------")
#  print(f"Total Votes:{vote_total}")
#  print("------------------------------------------")