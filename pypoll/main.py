# Py Me Up Charlie Week 3 HW Assignment: PyPoll
#Import dependencies
import os
import csv


#Set File path
csvpath = os.path.join('.','Resources', 'election_data.csv')

Votes = []
UniqueCand = []
CandidateList = []
VoteCount = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0
ElectWin = 0



#Read Budget_Data CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    
    

    for row in csvreader:
        #TotalVotes
        CandidateList.append(row[2])
        VoteCount=len(CandidateList)       
        
for name in CandidateList:
    if name not in UniqueCand:
        UniqueCand.append(name)

CandDict = {}

for name in UniqueCand:
    CandDict[name]=0

for name in CandidateList:
    CandDict[name]=CandDict[name]+1

KhanVotes = CandDict["Khan"]
CorreyVotes = CandDict["Correy"]
LiVotes = CandDict["Li"]
OTooleyVotes = CandDict["O'Tooley"]


#Election Winner - ElectWin
 
ElectWin = max([KhanVotes,CorreyVotes,LiVotes,OTooleyVotes])

#Declare the Winner
if ElectWin == KhanVotes:
     Winner = "Khan"
elif ElectWin == CorreyVotes:
    Winner = "Correy"
elif ElectWin == LiVotes:
    Winner = "Li"
else:
    Winner = "O'Tooley"

#Vote Perentage per Candidate Khan = KVP, Correy = CVP, Li = LVP, O'Tooley = TVP
KVP = round(KhanVotes/VoteCount*100,2)
CVP = round(CorreyVotes/VoteCount*100,2)
LVP = round(LiVotes/VoteCount*100,2)
TVP = round(OTooleyVotes/VoteCount*100,2)

#Print Election Reults Analysis
print(f'Election Results Analysis')
print(f'_______________________________________')
print(f'Total Votes: {VoteCount}')
print(f'Khan Votes: {KVP}% ({KhanVotes})')
print(f'Correy Votes:{CVP}% ({CorreyVotes})') 
print(f'Li Votes: {LVP}% ({LiVotes})')
print(f'OTooley Votes:{TVP}% ({OTooleyVotes})')
print(f'Winner: {Winner}')

output_file = os.path.join('.', 'Resources', 'PyPollAnalysis.csv')
with open(output_file, 'w', newline='') as txtfile:
    
    txtfile.write(f'Election Results Analysis\n')
    txtfile.write(f'_______________________________________\n')
    txtfile.write(f'Total Votes: {VoteCount}\n')
    txtfile.write(f'Khan Votes: {KVP}% ({KhanVotes})\n')
    txtfile.write(f'Correy Votes:{CVP}% ({CorreyVotes})\n') 
    txtfile.write(f'Li Votes: {LVP}% ({LiVotes})\n')
    txtfile.write(f'OTooley Votes:{TVP}% ({OTooleyVotes})\n')
    txtfile.write(f'Winner: {Winner}\n')