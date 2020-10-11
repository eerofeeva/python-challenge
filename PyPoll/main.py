# ## PyBank
import csv

#Voter ID,County,Candidate
# 12864552,Marsh,Khan
# 17444633,Marsh,Correy
# 19330107,Marsh,Khan
# 19865775,Queen,Khan
# 11927875,Marsh,Khan
# 19014606,Marsh,Li

#import csv
total_votes = 0
total_votes_candidate = dict()

with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader.__next__()

    for row in csvreader:
        total_votes = total_votes+1
        candidate = row[2]
        if candidate not in total_votes_candidate.keys():
            total_votes_candidate[candidate]=0
        total_votes_candidate[candidate]+=1
    
# The total number of votes cast
# A complete list of candidates who received votes
# The total number of votes each candidate won
# The percentage of votes each candidate won
percentages = dict()
for candidate in total_votes_candidate.keys():
    percentages[candidate]= float(total_votes_candidate[candidate])/total_votes *100
    # # The winner of the election based on popular vote.
    if max(percentages.values())==percentages[candidate]:
        winner_name = candidate

template='''
   Election Results
-------------------------
 Total Votes: {}
-------------------------
 '''
template2 ='''
 {}: {}% ({}) 
'''
template3 = '''
 -------------------------
 Winner: {}
 '''
t2_list=[template2.format(candidate,percentages[candidate],total_votes_candidate[candidate]) for candidate in total_votes_candidate.keys()]

report = template.format(total_votes)+''.join(t2_list) + template3.format(winner_name)

print(report)
# report = template.format(total_months, total_profits, average, months[max_index], max_profit, months[min_index], max_loss)
# print(report)

# with open("analysis/report.txt", 'w') as text: 
#     text.write(report)

