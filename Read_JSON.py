import pandas as pd
df=pd.read_json('employees.json')
# print(df)

# json file from df
df['Bonus']=df['Salary']*0.10
print(df)

#Save the updated Data Frame to a new JSON file
df.to_json('employees_with_bonus.json',orient='records',lines=True)