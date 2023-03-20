import os
import csv
PyBank_csv = os.path.join('Resources','budget_data.csv')



months = []
profit_loss = 0 
profit_loss = []
total_profit_loss = 0
prvious_row = 1088983 
total_change_p_l = 0
Change_profit_loss_list = []

with open(PyBank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    for row in csv_reader:
     
     # Creat list for month

     months.append(row[0])

     # calculate total 
     total_profit_loss = total_profit_loss + int(row[1])

     Change_profit_loss = int(row[1]) - prvious_row
     Change_profit_loss_list.append(Change_profit_loss)

     # Calculate total change
     total_change_p_l = total_change_p_l + Change_profit_loss
     
     prvious_row = int(row[1])

    
    list_count = len(Change_profit_loss_list)

    average_total_change = total_change_p_l / (list_count-1)

    
    gretest_increase = int(max(Change_profit_loss_list))
    #print(f'Greatest Increase in Profits :  {(gretest_increase)}')

    greatest_decrease = int(min (Change_profit_loss_list))
    
    
    #for  
       #print(Change_profit_loss_list[i])
     #if  int(row[0]) == gretest_increase:
       #index_i=i
     #i=i+1

    month_change_list= list(zip(months,Change_profit_loss_list))
    

    for row in month_change_list:
       if greatest_decrease == (row[1]):
          decrease = row
          #print(f'Greatest Decrease in Profits :  {(row)}')

          
       elif gretest_increase == (row[1]):
             increase = row
             #print(f'Greatest Increase in Profits :  {(row)}')


output_path = os.path.join("Analysis", "result.txt")

with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
     csvwriter = csv.writer(csvfile, delimiter=',')
     csvwriter.writerow(["-----------------------------"])
     csvwriter.writerow(['Financial Analysis'])
     csvwriter.writerow(["-----------------------------"])
     csvwriter.writerow([f'Total Months : {len(months)}'])
     csvwriter.writerow([f'Total :  {(total_profit_loss)}'])
     csvwriter.writerow([f'Average Change :  {round(average_total_change,2)}'])
     csvwriter.writerow([f'Greatest Increase in Profits :  {increase}'])
     csvwriter.writerow([f'Greatest Decrease in Profits :  {decrease}'])
     
     

#print(f'Total Months : {len(months)}')
    
#print(f'Total :  {(total_profit_loss)}')
    
#print(f'Average Change :  {round(average_total_change,2)}')



#print(f'Greatest Decrease in Profits :  {(months(index_i)),(greatest_decrease) }')

