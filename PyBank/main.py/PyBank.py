# Python script that analyzes the records to calculate each of the following values:
    # The total number of months included in the dataset.
    # The net total amount of "Profit/Losses" over the entire period.
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes.
    # The greatest increase in profits (date and amount) over the entire period.
    # The greatest decrease in profits (date and amount) over the entire period.

# Import the os module and the csv module.
import os
import csv

# Path To Collect Data From Folder
csvpath = os.path.join( "Resources", "budget_data.csv")
pathout = os.path.join( "Analysis", "budget_analysis.txt")

# Define PyBank's Variables.
date = []
monthly_pnl = []
months = 0
total = 0 
prev_rev = 0
change = 0
total_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]

# Open Path & Read CSV.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header and assign variables.
    for row in csvreader:
        date.append(row[0])
        monthly_pnl.append(row[1])

    # Create script to calculate the following:

        #The total number of months included in the dataset.
        months += 1
        total += int(row[1])

        # Calculate The Change.
        change = int(row[1]) - prev_rev
        if prev_rev == 0:
            change = 0
        prev_rev = int(row[1])
        total_change += change

        # Calculate The Greatest Increase and Greatest Decrease.
        if change > int(greatest_increase[1]):
            greatest_increase[1] = change
            greatest_increase[0] = row[0]
        if change < int(greatest_decrease[1]):
            greatest_decrease[1] = change
            greatest_decrease[0] = row[0]


    total_change = total_change / (months - 1)


# Print The Results In Terminal.
print("\n\nFinancial Analysis")
print("----------------------------")
print(f"Months total in Analysis:  {months}")
print(f"Total:  ${total}")
print(f"Average Change: ${total_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Output To A Text File.
with open(pathout, "w") as results:
     results.write("\n\nFinancial Analysis\n")
     results.write("----------------------------\n")
     results.write(f"Months total in Analysis:  {months}\n")
     results.write(f"Total:  ${total}\n")
     results.write(f"Average Change: ${total_change:.2f}\n")
     results.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
     results.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")