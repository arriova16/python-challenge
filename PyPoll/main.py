import os 
import csv



input_file = os.path.join("Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
# print(input_file)
output_file = os.path.join("analysis", "election_analysis.txt")

# create global variables
vote_total = 0
percent_votes = 0
winner_won = 0
candidates_votes = 0
vote = 0
# list to store data



# Election results print and line break
print("Election Results")
print("------------------------------------------")


# outter loop
with open(input_file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:
        vote_total = vote_total +1 

    


        # remaing loop
    print(f"Total Votes:{vote_total}")

# line break
print("------------------------------------------")
def candidates_votes(candidate_data):
    name = str(candidate_data[2])
    votes = int(candidate_data)
    
    if name == name :
        votes = vote + 1
    print(f"candidate names:{votes}")
    

