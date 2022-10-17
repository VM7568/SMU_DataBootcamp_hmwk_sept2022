import csv

csvpath = "Instructions/PyBank/Resources/budget_data.csv" 
rows = 0
total = 0
total_change = 0
greatest_increase = 0
best_month = ""
greatest_decrease = 0
worst_month = ""

# Read in the CSV file
with open(csvpath, encoding='utf-8') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents, split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Loop through the data after header
    for row in csvreader:
        if csvreader.line_num == 2: #go to row 2 to calculate changes
            previous_pl = int(row[1])
        #Adds a value and the variable and assigns the result to that variable.
        rows += 1 
        total += int(row[1])
        #change = current row profit/loss - previous row profit/loss
        change = int(row[1]) - previous_pl 
        total_change += change
        previous_pl = int(row[1])
        
        if change > greatest_increase: #find greatest increase amount and month associated with it
            greatest_increase = change 
            best_month= row[0]
        elif change < greatest_decrease: #find greatest decrease amount and month associated with it
            greatest_decrease = change 
            worst_month = row[0]   
        else:
            pass    

#Average of total change in profits/losses, rounded to 2 decimal places
avg_change = round((total_change / (rows-1)),2)

#Format Total profits/losses with Dollar $ign
total_dollars = "${:.2f}".format(total)

analysis=(f"Total Months: {rows}\nTotal: {total_dollars}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {best_month} (${greatest_increase})\nGreatest Decrease in Profits: {worst_month} (${greatest_decrease})\n")

print("\nFinancial Analysis\n----------------------------")
print(analysis)

# https://www.pythontutorial.net/python-basics/python-write-text-file/
file1=open('Solutions/pybankvm.txt', 'w', encoding='utf-8')
lines=((f'\nFinancial Analysis\n----------------------------\n') + (f'{analysis}'))
file1.writelines(lines)
file1.close()
    