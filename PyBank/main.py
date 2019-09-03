#Find total number of months (each line is 1 month)
#Net profit/loss over entire period
#Average change in profit/loss over entire period
#Greatest increase in profit/loss in entire period (Date and amount)
#Greatest decrease in profit/loss over entire period (Date and amount)
#Print results and write them to a text file that gets exported

# Modules
import os
import csv

#Variables
greatestProfit = 0
greatestLoss = 0
totalMonths = 0.0
averageProfit = 0.0
netProfit = 0.0
currentProfit = 0
greatestProfitDate = ""
greatestLossDate = ""

# Set path for file
csvpath = os.path.join("bankData.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        print(row[1])
        currentProfit = int(row[1])
        if currentProfit > greatestProfit:
            greatestProfit = currentProfit
            greatestProfitDate = row[0]
        elif currentProfit < greatestLoss:
            greatestLoss = currentProfit
            greatestLossDate = row[0]
        totalMonths = totalMonths + 1
        netProfit = netProfit + currentProfit
        averageProfit = netProfit / totalMonths
    

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total: " + str(netProfit))
    print("Average Change: " + str(averageProfit))
    print("Greatest Increase in Profits: " + greatestProfitDate + " " + str(greatestProfit))
    print("Greatest Decrease in Profits: " + greatestLossDate + " " + str(greatestLoss))

file = open("output.txt","w")
file.write("Financial Analysis\n")
file.write("----------------------------" + "\n")
file.write("Total Months: " + str(totalMonths) + "\n")
file.write("Total: " + str(netProfit) + "\n")
file.write("Average Change: " + str(averageProfit) + "\n")
file.write("Greatest Increase in Profits: " + greatestProfitDate + " " + str(greatestProfit) + "\n")
file.write("Greatest Decrease in Profits: " + greatestLossDate + " " + str(greatestLoss) + "\n")
file.close()