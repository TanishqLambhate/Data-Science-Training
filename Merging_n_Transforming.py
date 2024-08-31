import pandas as pd


df1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4],
    'employee_name': ['John Doe', 'Jane Smith', 'Sam Brown', 'Emily Davis']
})
df2 = pd.DataFrame({
    'employee_id': [3, 4, 5, 6],
    'department': ['Finance', 'HR', 'IT', 'Marketing']
})
merged_df = pd.merge(df1, df2, on='employee_id', how='inner')
print(merged_df)

df = pd.DataFrame({
    'employee_id': [1,2,2,3,3],
    'department': ['HR', 'IT', 'IT', 'Finance','Finance','Finance'],
    'salary':[50000,60000,62000,55000,58000,60000]
})

groupedd_df=df.groupby('department')['salary'].mean().reset_index()
print(groupedd_df)