import csv
import os

print("\nThis program will count the frequency of unique phrases in a text file!\n")
 
while True:
    fname = input("Enter a file name: ")
    if os.path.isfile(fname) and fname.endswith('.txt'):
        break
    else:
        print('File Not Found!  Files Must Be (.txt) Format!\n')    #error message
        c
with open(fname) as f:
    schools = [line.strip() for line in f.readlines()]
            
school_count = {}  #school / frequency dictionary
for school in schools:
    if school in school_count.keys():
        school_count[school] += 1
    else:
        school_count[school] = 1


#export to CSV
csv_file = input('CSV File Name (Name your file): ')#names csv file
csv_file = csv_file + '.csv'

with open(csv_file, 'w') as f:
    w = csv.writer(f)
    w.writerow(["Phrase", "Frequency"])
    for k,v in school_count.items():
        w.writerow([k,v])

print('\nDone!')


