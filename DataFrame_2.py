import pandas as pd
data={
    "Name":["Amit","Priya","Vikram","Neha","Ravi"],
    "Age":[25,30,35,40,45],
    "City":["Mumbai","Delhi","Banglore","Chennai","Pune"]
}
df=pd.DataFrame(data)
df["Salary"]=[50000,60000,70000,80000,90000]
#Create another DataFrame to concatenate
df_new=pd.DataFrame({
    "Name":["Sonia","Rahul"],
    "Age":[29,31],
    "City":["Kolkata","Hyderabad"],
    "Salary":[58000,63000]
})

#Concatenate the two DataFrames

df_concat=pd.concat([df,df_new],ignore_index=True)
print(df_concat)

filtered_salary_df=df_concat[df_concat["Salary"]>=50000]
print(filtered_salary_df)

def finding_a(name):
        return name.startswith("A")

filtered_names=df[df['Name'].apply(finding_a)]
print(filtered_names)