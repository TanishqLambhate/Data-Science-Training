import pandas as pd
import numpy as np
#Load the csv file
df=pd.read_csv('sample_data.csv')

print(df)

#Replace empty strings and strings with only spaces with NaN
df.replace(r'^\s*$',np.nan,regex=True,inplace=True)

#check for missing values in each column
print(df.isnull().sum())

#Display rows with missing data
print(df[df.isnull().any(axis=1)])

#Drop rows with any missing values
df_cleaned=df.dropna()
print(df_cleaned)