import csv

csvpath = "Instructions/PyPoll/Resources/election_data.csv"
rows = 0
votes = {} #create dictionary
percent_votes = 0
winner_count = 0
winner = ""

# Read in the CSV file
with open(csvpath, encoding='utf-8') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents, split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
      
    #Loop through the data
    for row in csvreader:
        #Adds a value and the variable and assigns the result to that variable.
        rows += 1
        candidate = row[2]
        
        if candidate in votes.keys(): #create candidate dictionary
            votes[candidate] += 1
        else:
            votes[candidate] = 1
                   
        if (votes[candidate] > winner_count): #find candidate with most votes
            winner_count = votes[candidate]
            winner = max([candidate])
        else:
            pass
 
# for x in votes.keys():
#     results=(f"{x}: {votes[x]} total votes, which is {round((100*votes[x]/rows),3)}%")
#     print(results)
           
print("\nElection Results\n----------------------------")            
print(f"Total Votes: {rows}\n----------------------------")
for x in votes.keys():
    results=(f"{x}: {votes[x]} total votes, which is {round((100*votes[x]/rows),3)}%")
    print(results)
print("----------------------------")
print(f"Winner: {winner}\n----------------------------\n")

# https://www.pythontutorial.net/python-basics/python-write-text-file/
file1=open('Solutions/pypollvm.txt', 'w', encoding='utf-8')
lines=((f"\nElection Results\n----------------------------\nTotal Votes: {rows}\n----------------------------\n") + 
       (f"{results}\n----------------------------\nWinner: {winner}\n----------------------------\n"))
file1.writelines(lines)
file1.close()