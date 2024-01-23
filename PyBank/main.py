#creating and importing file
import os
import csv
#set file path
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#open file to read
with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')


    #create list for data
    all_months = []
    profit = []

    #set values to 0
    total_months = 0
    net_total = 0
    previous_rev = 0




   #skip header
    next(reader)

#create loop through rows; identity columns for dates and profits (profits must be converted to int since is a numerical value)
    for row in reader:
        current_months = row[0]
        current_profit = int(row[1])


        #track total months and net total
        total_months += 1
        net_total += current_profit

        #track change
        if previous_rev != 0 :
            change = current_profit - previous_rev
            profit.append(change)
            all_months.append(row[0])
            total_change = change - previous_rev

        previous_rev = current_profit



    #calc avg change
    average_change = total_change/ (total_months-1)

     
    
#find greatest increase
    greatest_increase = max(profit)
    greatest_increase_month = all_months[profit.index(greatest_increase)]




#find greatest decrease
    greatest_decrease = min(profit)
    greatest_decrease_month = all_months[profit.index(greatest_decrease)]



#create and print output
output = (
    f"Financial Analysis"
    f"----------------------------"
    f'Total Months: {total_months}'
    f'Total: ${net_total} '
    f'Average Change: ${average_change} '
    f'Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase} '
    f'Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}')

print(output)

#export file to .txt
output_file = "PyBank/result.txt"
with open(output_file, "w") as f:
    f.write(output)









    