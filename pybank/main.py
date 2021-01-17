# Py Me Up Charlie Week 3 HW Assignment: PyBank
#Import dependencies
import os
import csv

#Set File path
csvpath = os.path.join('..', 'pybank', 'Resources', 'budget_data.csv')

#Read Budeget_Data CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader,None)
    csv_header = next(csvreader)
    row = next(csvreader)

    Months = []
    Profits = []
    Change = []
    MaximumChange = int(row[1])
    PreviousRow = int(row[1])
    monthcount = 0
    TotalAmountProfits = 0
    GNC = 0
    GPC = 0





    for row in csvreader:
        #Totalmonths
        Months.append(row[0])
        monthcount=len(set(Months))
    

        #TotalAmount(Profits)
        Profits.append(int(row[1]))
        TotalAmountProfits = sum(Profits)
    


        # ProfitChange (ProfitRow - PreviousRow)
        
        ProfitChange = int(row[1]) - PreviousRow
        Change.append(ProfitChange)

        #AverageChange
        AverageChange = sum(Change)/monthcount

    #GreatestPositiveChange (GPC) Amount = maximum value in Change
    #GreatestPositiveChange (GPC) Date (GPCD)= month associated to the maximum value in Change
    GPC = max(Change)
    GPCD = Months[Change.index(GPC)]  


    #Greatest Negative Change (GNC) Amount  = minimum value in Change
    #Greatest Negative Change (GNC) Amount  Date (GNCD) = month associated to the  minimum value in Change
    GNC = min(Change)
    GNCD = Months[Change.index(GNC)]

    #Print Analysis
    print('ANALYSIS')
    print('______________________________________________________')
    print(f'Total Number of Months: {str(monthcount)}')
    print(f'Net total Profits/Losses: ${str(int(TotalAmountProfits))} ')
    print(f'Average Change in Profits: ${str(int(AverageChange))}')
    print(f'Greatest Increase in Profits: {GPCD}, (${GPC})')
    print(f'Greatest Increase in Profits: {GNCD}, (${GNC})')

#Write Text file
output_file = os.path.join('..', 'pybank', 'Resources', 'Pybankmaintext.txt')

with open(output_file,'w') as txtfile:
    txtfile.write('ANALYSIS')
    txtfile.write('______________________________________________________\n')
    txtfile.write(f'Total Number of Months: {str(monthcount)}\n')
    txtfile.write(f'Net total Profits/Losses: ${str(int(TotalAmountProfits))}\n ')
    txtfile.write(f'Average Change in Profits: ${str(int(AverageChange))}\n')
    txtfile.write(f'Greatest Increase in Profits: {GPCD}, (${GPC})\n')
    txtfile.write(f'Greatest Increase in Profits: {GNCD}, (${GNC})\n')
    








