import pandas as pd
py_roll=pd.read_csv('election_data.csv')

print(py_roll.head())

print("Election Result")
print("----------------------------------------")
total_cast=len(py_roll['Voter ID'])
print("Total Vote Cast: "+str(total_cast))
print("----------------------------------------")
print(py_roll['Candidate'].value_counts()/total_cast,py_roll['Candidate'].value_counts())
print("----------------------------------------")
winner=py_roll['Candidate'].value_counts().max()
print("Winner:"+str(winner))