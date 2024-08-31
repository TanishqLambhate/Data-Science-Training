import pandas as pd
# load the csv file into a dataframe
df=pd.read_csv('employee.csv')
# print(df)

#manipulation
#Display the first three rows
print(df.head(3))

#Show the summary information about the DataFrames
print(df.info())

#Display summary statistics of numeric coloumns
print(df.describe())

#Filer rows where Salary is grateer than 80000
high_salary_df=df[df['Salary']>80000]
print(high_salary_df)

sorted_df=df.sort_values(by="Age",ascending=False)
print(sorted_df)