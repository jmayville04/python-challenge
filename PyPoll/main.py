#creating and importing file
import os
import csv
#set file path
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#open file to read
with open(election_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')


    #create list for candidate, votes  and percentage
    candidate_votes = []
    candidate = []
    vote_percentage = []

    #set values to 0
    total_ballots = 0
 
    

    #skip header
    next(reader)


    #create loop through rows; identity columns for votes and candidates (profits must be converted to int since is a numerical value)
    for row in reader:
        total_ballots += 1

    
        #if candidate is not in list, add candidate to list and find index; If candidate is on list, add tally to vote
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            candidate_votes.append(1)

        else:
            index = candidate.index(row[2])
            candidate_votes[index] += 1

    #find vote percentage
    for votes in candidate_votes:
        percentage = (votes/total_ballots)*100
        percentage = round(percentage, 3)
        percentage_str = "{:.3f}%".format(percentage)
        vote_percentage.append(percentage_str)




#find winning candidate
    winner = max(candidate_votes)
    winner_name = candidate[candidate_votes.index(winner)]


#create and print output
output = (
    f'Election results\n'
    f'----------------------------\n'
    f'Total Votes: {total_ballots}\n'
    f'----------------------------"\n'
)

for i in range(len(candidate)):
        output += f'{candidate[i]}: {str(vote_percentage[i])} ({str(total_ballots)})\n'

output += (
    f'----------------------------\n'
    f'Winner: {winner_name}\n'
)


print(output)

#export file to .txt
output_file = "PyPoll/result.txt"
with open(output_file, "w") as f:
    f.write(output)




