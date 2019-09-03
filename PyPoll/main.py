# Modules
import os
import csv


def main():
    #Variables
    totalVotes = 0
    candidateList = []
    candidateVotes = []
    candidatePercent = []
    currentCandidate = ""
    candidateAlreadyExists = False
    candidateWinner = 1

    # Set path for file
    csvpath = os.path.join("pollData.csv")
    next

    # Open the CSV
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader) #Skipping the header - row[0] = ID, row[1] = County, row[2] = Candidate

        for row in csvreader:
            totalVotes = totalVotes + 1
            currentCandidate = row[2]

            for i in range(len(candidateList)): 
                if(candidateList[i] == currentCandidate): 
                    candidateAlreadyExists = True
                    candidateVotes[i] = candidateVotes[i] + 1

            if(candidateAlreadyExists == False):
                candidateList.append(row[2])
                candidateVotes.append(1)

            candidateAlreadyExists = False

        for i in range(len(candidateList)):
            candidatePercent.append(findAverage(candidateVotes[i], totalVotes))

        for i in range(len(candidateList)):
            if (candidateVotes[i] > candidateVotes[candidateWinner]):
                candidateWinner = i


        with open("output.txt", "w") as f:
            print("Election Results", file = f)
            print("-------------------------", file = f)
            print(f"Total Votes: {totalVotes}", file = f)
            print("-------------------------", file = f)

            for i in range(len(candidateList)):
                print(f"{candidateList[i]}: {round(candidatePercent[i], 3)}% ({candidateVotes[i]} Votes)", file = f)

            print("-------------------------", file = f)
            print(f"Winner: {candidateList[candidateWinner]}", file = f)
            print("-------------------------", file = f)

        outputFile = open("output.txt","r")
        print (outputFile.read())

def findAverage(candidateVotes,totalVotes):
    average = (candidateVotes/totalVotes) * 100
    return average

main()
