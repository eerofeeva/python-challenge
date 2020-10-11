# ## PyBank
import csv

with open("Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    data = [ [row[0] , row[1]] for row in csvreader]

#   * The total number of months included in the dataset
total_months = len(data)-1

#   * The net total amount of "Profit/Losses" over the entire period
profit_loss_amounts_list = [int(x[1]) for x in data[1:]]
months = [x[0] for x in data[1:]]

total_profits = sum(profit_loss_amounts_list)

#   * The average of the changes in "Profit/Losses" over the entire period

change_by_month = [ y2-y1 for y1, y2  in zip(profit_loss_amounts_list[0:-1],profit_loss_amounts_list[1:])]

average =float(sum(change_by_month))/(total_months-1)

#   * The greatest increase in profits (date and amount) over the entire period
max_profit = max(change_by_month)

#   * The greatest decrease in losses (date and amount) over the entire period
max_loss = min(change_by_month)

for index, m in enumerate(change_by_month):
    if m == max_profit:
        max_index = index+1
    if m == max_loss: 
        min_index = index+1

# * As an example, your analysis should look similar to the one below:
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#print(total_months, total_profits, average,max_profit, max_loss)

template='''
   Financial Analysis
   ----------------------------
   Total Months: {}
   Total: ${}
   Average  Change: ${:.2f}
   Greatest Increase in Profits: {} (${})
   Greatest Decrease in Profits: {} (${})
'''
report = template.format(total_months, total_profits, average, months[max_index], max_profit, months[min_index], max_loss)
print(report)

with open("analysis/report.txt", 'w') as text: 
    text.write(report)

