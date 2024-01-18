#Import dependencies
import os
import csv

#Establish the path to the budget data csv file in the Resources directory
budget_data_csv = os.path.join("Resources","budget_data.csv")

#Define variables
total_months = 0
total_profit_losses = 0
previous_profit_losses = None
changes = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#Read in csv file data using the csv module and create csv_reader object
with open(budget_data_csv, 'r') as budget_csv:     #open the referenced file in read mode 
    csv_reader = csv.reader(budget_csv)
    row_header = next(csv_reader, None)              #Store header row

    for row in csv_reader:
        total_months += 1

#print(f"Total Months: {total_months}")

with open(budget_data_csv, 'r') as budget_csv:     #open the referenced file in read mode 
    csv_reader = csv.reader(budget_csv)
    next(csv_reader, None)              #Store header row

    for row in csv_reader:
        profit_losses = int(row[1])
        total_profit_losses += profit_losses

formatted_total = "${:.0f}".format(total_profit_losses)

#Read in csv file data using the csv module and create csv_reader object
with open(budget_data_csv, 'r') as budget_csv:     #open the referenced file in read mode 
    csv_reader = csv.reader(budget_csv)
    row_header = next(csv_reader, None)              #Store header row

    for row in csv_reader:
        current_profit_losses = int(row[1])
        if previous_profit_losses is not None:
            change = current_profit_losses - previous_profit_losses
            changes.append(change)
        previous_profit_losses = current_profit_losses

average_change = sum(changes)/len(changes)
formatted_average_change = "${:.2f}".format(average_change)

with open(budget_data_csv, 'r') as budget_csv:     #open the referenced file in read mode 
    csv_reader = csv.reader(budget_csv)
    next(csv_reader, None)              #Store header row

    for row in csv_reader:
        current_profit_losses = int(row[1])
        date = row[0]
        #Conditional to find Greatest Increase and Decrease in Profits
        if previous_profit_losses is not None:
            change = current_profit_losses - previous_profit_losses

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

        previous_profit_losses = current_profit_losses

#print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
        

##Print Outputs in the required format
print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {total_months}")

print("----------------------------")

print(f"Total: {formatted_total}")

print("----------------------------")

print(f"Average Change: {formatted_average_change}")

print("----------------------------")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

print("----------------------------")

print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Output results to a text file
output_file = os.path.join("analysis", "budget_data_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total: {formatted_total}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Average Change: {formatted_average_change}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}\n")
