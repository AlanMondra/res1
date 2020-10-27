import csv
import statistics

file_ = open('insurance.csv')
lBMI = []
lAGE = []
reader = csv.DictReader(file_)
cnt = 0
for line in reader:
    lAGE.append(line['age'])
    lBMI.append(line['bmi'])
    cnt += 1
    break
print('-----AGE------\nMODA:',statistics.mode(lAGE))
print('-----AGE------\nMEDIANA:',statistics.median(lAGE))
#print('-----AGE------\nMEDIA:',statistics.mean(lAGE))
print('\n-----BMI------\nMODA:',statistics.mode(lBMI))
print('-----BMI------\nMEDIANA:',statistics.median(lBMI))
#print('-----BMI------\nMEDIA:',statistics.mean(lBMI))

