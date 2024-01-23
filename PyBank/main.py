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
    previous_profit = 0
    greatest_increase = 0
    greatest_decrease = 0



   #skip header
    next(reader)

#create loop through rows; identity columns for dates and profits (profits must be converted to int since is a numerical value)
    for row in reader:
        current_months = row[0]
        current_profit = int(row[1])


        #track total months and net total
        total_months += 1
        net_total += current_profit

        #track change- ask why this is necessary
        change = current_profit - previous_profit
        profit.append(change)

        #Save current month for greatest increase/decrease
        all_months.append(current_months)

     
    
#find greatest increase
    greatest_increase = max(profit)
    greatest_increase_index = profit.index(greatest_increase)
    greatest_month = all_months[greatest_increase_index]

#find greatest decrease
    greatest_decrease = min(profit)
    greatest_decrease_index = profit.index(greatest_decrease)
    lowest_month = all_months[greatest_decrease_index]


#calculate average change
    average_change= sum(profit)/len(profit)

#print outcomes
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total} ')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_month} ${greatest_increase}')
    print(f'Greatest Decrease in Profits: {lowest_month} ${greatest_decrease}')







    