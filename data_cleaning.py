import pandas as pd
import numpy as np

#Load the csv
df=pd.read_csv('Sample_data.csv')

print("Before Transformation")
print(df)

#Ensure there are no leading/ trailing spaces in column names
df.columns=df.columns.str.strip()

#Strip spaces from the 'City' column and replace empty strings with Nan
df['City']=df['City'].str.strip().replace('',np.nan)

#Fill missing values in the 'City' column with 'Unknown'
df['City']=df['City'].fillna('Unknown')

#Fill missing values in the 'Age' column with the median age
df['Age']=pd.to_numeric(df['Age'].str.strip(),errors='coerce')
df['Age']=df['Age'].fillna(df['Age'].median())

#Fill missing values in the 'salary' column with the median salary
df['Salary']=df['Salary'].fillna(df['Salary'].median())

#Display the DataFrame after filling missing values
print(df)