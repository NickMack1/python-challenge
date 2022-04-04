

import os
import csv


# Path to collect data from the Resources folder
Budget_csv = os.path.join('Pybank','Resources', 'budget_data.csv')

months = []
total_lst = []
Ave_lst = []
Greatest_lst = []
Decrease_lst = []




    
with open(Budget_csv, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)

    for row in csvreader:
        
        months.append(row[0])
        
        total_lst.append(int(row[1]))

        Ave_lst = [y-x for x, y in zip(total_lst[:-1], total_lst[1:])]

        Greatest_lst.append(int(row[1]))
         
        Decrease_lst.append(int(row[1]))
 
    for a, b in enumerate(Greatest_lst):
     if b == max(Greatest_lst):
          months_max_index = (a)

    for c in [months[months_max_index]]:
     Grt_increase_month = c
 
    for d, e in enumerate(Decrease_lst):
     if e == min(Decrease_lst):
          months_min_index = (d)
 
    for f in [months[months_min_index]]:
     Grt_decrease_month = f

print("Financial Analysis")
print("----------------------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: {sum(total_lst)}')
print(f'Average Change: ${round(sum(Ave_lst)/len(Ave_lst),2)}')
print(f'Greatest Increase in Profits:  {Grt_increase_month} (${max(Ave_lst)})')
print(f'Greatest Decrease in Profits: {Grt_decrease_month} (${min(Ave_lst)})')



f = open("Financial Analysis HW.txt", "a")
print("Financial Analysis", file=f)
print("----------------------------------------", file=f)
print(f'Total Months: {len(months)}', file=f)
print(f'Total: {sum(total_lst)}', file=f)
print(f'Average Change: ${round(sum(Ave_lst)/len(Ave_lst),2)}', file=f)
print(f'Greatest Increase in Profits:  {Grt_increase_month} (${max(Ave_lst)})', file=f)
print(f'Greatest Decrease in Profits: {Grt_decrease_month} (${min(Ave_lst)})', file=f)
f.close()
