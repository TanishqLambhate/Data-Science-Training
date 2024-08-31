import pandas as pd

#Creating a DataFrame from a dictionary with Indian names

data={
    "Name":["Amit","Priya","Vikram","Neha","Ravi"],
    "Age":[25,30,35,40,45],
    "City":["Mumbai","Delhi","Banglore","Chennai","Pune"]
}
df=pd.DataFrame(data)
# print(df)

#First thing you get data convert it into dataframe

#Accessing a single column
print(df["Name"])

#Accessing multiple columns
print(df[["Name","Age","City"]])

#Accessing rows using index
print(df.iloc[0]) #First row
print(df.iloc[0:3])

#Filter rows where Age is greater than 30
filtered_df=df[df["Age"]>30]
print(filtered_df)

#Adding a new column 'salary'
df["Salary"]=[50000,60000,70000,80000,90000]
print(df)

#Sorting by Age
sorted_df=df.sort_values(by="Age",ascending=False)
print(sorted_df)

#Rename the 'Name column to 'Full Name' and 'Age' to 'Years'
df_renamed=df.rename(columns={"Name":"Full Name","Age":"Years"})
print(df_renamed)

#Drop the 'City' column
df_dropped=df.drop(columns=["City"])
print(df_dropped)

#Create a new column 'Seniority' based on the age
df['Seniority']=df['Age'].apply(lambda x:'Senior' if x>=35 else 'Junior')
print(df)

df["Salary"]=[50000,60000,70000,80000,90000]
#Group By 'City' and calculate the average Salary in each city
df_grouped=df.groupby("City")["Salary"].mean()

#apply a custom function to the 'salary' column to add a 10% bonus
def add_bonus(salary):
    return salary*1.10

df['Salary_with_Bonus']=df['Salary'].apply(add_bonus)
print(df)

#Create another DataFrame
df_new=pd.DataFrame({
    "Name":["Amit","Priya","Ravi"],
    "Bonus":[5000,6000,7000]
})

#Merge based on the 'name' column
df_merged=pd.merge(df,df_new,on="Name",how="left")
print(df_merged)

