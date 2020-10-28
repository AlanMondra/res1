import pandas as pd

df = pd.read_csv('insurance.csv')

df.info()
df.describe()
print('\n----------------------------MODE----------------------------\n')
print(df.mode())
print('\n------------MEAN------------\n')
print(df.mean())
print('\n----------MEDIAN---------\n')
print(df.median())
#print('\n-----AGE-----\n',df['age'].mode())
#print('\n',df['age'].mean())
#print('\n',df['age'].median())

#print('\n-----BMI-----\n',df['bmi'].mode())
#print('\n',df['bmi'].mean())
#print('\n',df['bmi'].median())