# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Er0oNsqramoY-8wmw6BvHQlHZLzBlNAG
"""

import pandas as pd
from datetime import datetime

   # Sample sales data
data = {
       "TransactionID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       "CustomerID": [101, 102, 103, 101, 104, 102, 103, 104, 101, 105],
       "ProductID": [501, 502, 501, 503, 504, 502, 503, 504, 501, 505],
       "Quantity": [2, 1, 4, 3, 1, 2, 5, 1, 2, 1],
       "Price": [150.0, 250.0, 150.0, 300.0, 450.0, 250.0, 300.0, 450.0, 150.0, 550.0],
       "Date": [
           datetime(2024, 9, 1),
           datetime(2024, 9, 1),
           datetime(2024, 9, 2),
           datetime(2024, 9, 2),
           datetime(2024, 9, 3),
           datetime(2024, 9, 3),
           datetime(2024, 9, 4),
           datetime(2024, 9, 4),
           datetime(2024, 9, 5),
           datetime(2024, 9, 5)
       ]
}
df = pd.DataFrame(data)

   # Save the DataFrame to a CSV file
df.to_csv('sales_data.csv', index=False)

print("Sample sales dataset has been created and saved as 'sales_data.csv'.")
# 2. **Verify the Dataset:**
#    - After running the script, ensure that the file `sales_data.csv` has been
#    created in your working directory.
with open('sales_data.csv', 'r') as file:
    print(file.read())

pip install pyspark

# 1. **Initialize the SparkSession:**
#    - Create a Spark session named `"Sales Dataset Analysis"`.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum ,count,avg
spark = SparkSession.builder \
    .appName("Sales Dataset Analysis") \
    .getOrCreate()
file_path = "sales_data.csv"
# 2. **Load the CSV File into a PySpark DataFrame:**
#    - Load the `sales_data.csv` file into a PySpark DataFrame.
#    - Display the first few rows of the DataFrame to verify that the data is
#     loaded correctly.
sales_df = spark.read.csv(file_path, header=True, inferSchema=True)
sales_df.show(5)
# Explore the data to understand its structure.

# 1. **Print the Schema:**
#    - Display the schema of the DataFrame to understand the data types.
print("The schema of the DataFrame to understand the data types")
sales_df.printSchema()
# 2. **Show the First Few Rows:**
#    - Display the first 5 rows of the DataFrame.
print("The first 5 rows of the DataFrame:")
sales_df.show(5)
# 3. **Get Summary Statistics:**
#    - Get summary statistics for numeric columns (`Quantity` and `Price`).
print("Summary Statistics:")
sales_df.select("Quantity", "Price").describe().show()

# 1. **Calculate the Total Sales Value for Each Transaction:**
#    - Add a new column called `TotalSales`, calculated by multiplying `Quantity` by `Price`.
sales_df=sales_df.withColumn("TotalSales",col("Quantity")*col("Price"))
print("The Total Sales Value for Each Transaction:")
sales_df.show()

# 2. **Group By ProductID and Calculate Total Sales Per Product:**
#    - Group the data by `ProductID` and calculate the total sales for each product.
total_sales_per_product_df = sales_df.groupBy("ProductID").agg(sum("TotalSales").alias("TotalSalesPerProduct"))
print("The total sales for each product:")
total_sales_per_product_df.show()

# 3. **Identify the Top-Selling Product:**
#    - Find the product that generated the highest total sales.
top_selling_product = total_sales_per_product_df.orderBy(col("TotalSalesPerProduct").desc()).first()
print(f"The top-selling product is ProductID {top_selling_product['ProductID']} with total sales of ₹{top_selling_product['TotalSalesPerProduct']}")

# 4. **Calculate the Total Sales by Date:**
#    - Group the data by `Date` and calculate the total sales for each day.
total_sales_by_date_df = sales_df.groupBy("Date").agg(sum("TotalSales").alias("TotalSalesPerDay"))
print("The total sales for each day")
total_sales_by_date_df.show()

# 5. **Filter High-Value Transactions:**
#    - Filter the transactions to show only those where the total sales value is greater than ₹500.
high_value_transactions_df = sales_df.filter(col("TotalSales") > 500)
print(" Transactions where the total sales value is greater than ₹500:")
high_value_transactions_df.show()


# ### **Additional Challenge (Optional):**

# If you complete the tasks above, try extending your analysis with the following challenges:

# 1. **Identify Repeat Customers:**
#    - Count how many times each customer has made a purchase and display the customers who have made more than one purchase.
repeat_customers_df = sales_df.groupBy("CustomerID").agg(count("TransactionID").alias("NumberOfPurchases"))
repeat_customers_df = repeat_customers_df.filter(col("NumberOfPurchases") > 1)
print("The customers who have made more than one purchase:")
repeat_customers_df.show()
# 2. **Calculate the Average Sale Price Per Product:**
#    - Calculate the average price per unit for each product and display the results.
average_price_per_product_df = sales_df.groupBy("ProductID").agg(avg("Price").alias("AveragePricePerUnit"))
print("The Average Sale Price Per Product:")
average_price_per_product_df.show()
# ---

