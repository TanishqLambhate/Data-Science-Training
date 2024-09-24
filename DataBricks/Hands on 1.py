# Databricks notebook source
# Move the file from Workspace to DBFS
dbutils.fs.cp("file:/Workspace/Shared/employee_data.csv", "dbfs:/FileStore/employee_data.csv")
# Load the file from DBFS
df_csv = spark.read.format("csv").option("header", "true").load("/FileStore/employee_data.csv")
df_csv.show()


# COMMAND ----------

# 1. Load the CSV data:
# Load the employee_data.csv file into a DataFrame.
# Display the first 10 rows and inspect the schema.
df_csv.display(10)
df_csv.printSchema()

# 2. Data Cleaning:
# Remove rows where the Salary is less than 55,000.
df_cleaned = df_csv.filter("Salary > 55000")
df_cleaned.display()

# Filter the employees who joined after the year 2020.
df_csv.filter("JoiningDate > '2020-01-01'").display()

# 3. Data Aggregation:
# Find the average salary by Department.
df_numeric = df_csv.withColumn("Salary", df_csv["Salary"].cast("double"))
df_avg_salary = df_numeric.groupBy("Department").avg("Salary")
df_avg_salary.display()

# Count the number of employees in each Department.
df_count_employees = df_numeric.groupBy("Department").count()
df_count_employees.display()

# 4. Write the Data to CSV:
# Save the cleaned data (from the previous steps) to a new CSV file.
df_cleaned.write.csv("cleaned_employee_data.csv")

# COMMAND ----------

# 1. Load the JSON data:
dbutils.fs.cp("file:/Workspace/Shared/product_data.json", "dbfs:/FileStore/product_data.json")

# Load the file from DBFS
df_json = spark.read.option("multiline", "true").json("/FileStore/product_data.json")
df_json.show()

# 2. Data Cleaning:
# Remove rows where Stock is less than 30.
df_cleaned=df_json.filter("Stock>30")

# Filter the products that belong to the "Electronics" category.
df_cleaned.filter("Category=='Electronics'").display()

# 3. Data Aggregation:
# Calculate the total stock for products in the "Furniture" category.
df_cleaned.filter("Category=='Furniture'").groupBy().sum("Stock").display()

# Find the average price of all products in the dataset.
df_cleaned.groupBy().avg("Price").display()

# 4. Write the Data to JSON:
# Save the cleaned and aggregated data into a new JSON file.
df_cleaned.write.json("cleaned_product_data.json")

# COMMAND ----------

# 1. Convert CSV and JSON Data to Delta Format:
# Convert the employee_data.csv and product_data.json into Delta Tables.
# Writing data to a Delta table

# Convert CSV (employee_data.csv) to Delta format

df_csv.write.format("delta").mode("overwrite").save("/Workspace/Shared/delta_employee_data")

# Convert JSON (product_data.json) to Delta format

df_json.write.format("delta").mode("overwrite").save("/Workspace/Shared/delta_product_data")

df_delta_employee = spark.read.format("delta").load("/Workspace/Shared/delta_employee_data")
df_delta_employee.show()

df_delta_product = spark.read.format("delta").load("/Workspace/Shared/delta_product_data")
df_delta_product.show()

# 2. Register Delta Tables:
# Register both the employee and product Delta tables as SQL tables.

spark.sql("CREATE OR REPLACE TEMP VIEW employee_delta_table AS SELECT * FROM delta.`/Workspace/Shared/delta_employee_data`")


spark.sql("CREATE OR REPLACE TEMP VIEW product_delta_table AS SELECT * FROM delta.`/Workspace/Shared/delta_product_data`")


# 3. Data Modifications with Delta Tables:
# Perform an update operation on the employee Delta table: Increase the
# salary by 5% for all employees in the IT department.
# Perform a delete operation on the product Delta table: Delete products
# where the stock is less than 40.
# Increase salary by 5% for employees in the IT department
spark.sql("""
    UPDATE delta.`/Workspace/Shared/delta_employee_data`
    SET Salary = Salary * 1.05
    WHERE Department = 'IT'
""")

spark.sql("""
    DELETE FROM delta.`/Workspace/Shared/delta_product_data`
    WHERE Stock < 40
""")

# 4. Time Travel with Delta Tables:
# Query the product Delta table to show its state before the delete
# operation (use time travel).
df_previous_state = spark.read.format("delta").option("versionAsOf", 0).load("/Workspace/Shared/delta_product_data")
df_previous_state.show()

# Retrieve the version of the employee Delta table before the salary
# update.
df_previous_employee = spark.read.format("delta").option("versionAsOf", 0).load("/Workspace/Shared/delta_employee_data")
df_previous_employee.show()

# 5. Query Delta Tables:
# Query the employee Delta table to find the employees in the Finance
# department.
finance_employees = spark.sql("SELECT * FROM employee_delta_table WHERE Department = 'Finance'")
finance_employees.show()

# Query the product Delta table to find all products in the Electronics
# category with a price greater than 500.
expensive_electronics = spark.sql("""
    SELECT * FROM product_delta_table
    WHERE Category = 'Electronics' AND Price > 500
""")
expensive_electronics.show()
