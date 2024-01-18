#Import dependencies
import os
import csv

#Establish the path to the election data csv file in the Resources directory
election_data_csv = os.path.join("Resources","election_data.csv")

#Define variables, dictionaries, lists
candidate_votes = {}
results = []

#Read in csv file data using the csv module and create csv_reader object
with open(election_data_csv, 'r') as election_csv:     #open the referenced file in read mode 
    csv_reader = csv.reader(election_csv)
    next(csv_reader, None)              #Skip headers

    #Iterate through rows to extract candidate names and calculate vote counts per candidate
    for row in csv_reader:
        candidate = row[2]  #pointing to the 
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#Add up all votes cast
total_votes_cast = sum(candidate_votes.values())

#Calculate percentage of votes received and format the results
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes_cast) * 100
    candidate_results = f"{candidate}: {percentage:.3f}% ({votes})"
    results.append(candidate_results)           #Append formatted string to a list

#Find winner of the election based on popular votes
winner = max(candidate_votes, key=candidate_votes.get)

##Print Outputs in the required format
print("Election Results")

print("-------------------------")

print("Total Votes: " + str(total_votes_cast))

print("-------------------------")

for candidate_results in results:
    print(candidate_results)

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Output results to a text file
output_file = os.path.join("analysis", "election_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes_cast}\n")
    txtfile.write("-------------------------\n")
    for candidate_results in results:
        txtfile.write(candidate_results + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

