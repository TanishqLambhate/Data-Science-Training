from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DeltaOperationsSimpleExample") \
    .getOrCreate()

# Define Delta table path
delta_table_path = "/delta/simple_data"

# Define initial sample data
initial_data = [
    (1, 100),
    (2, 200),
    (3, 300)
]

# Define schema
schema = ["ID", "Value"]

# Create DataFrame for initial data
df_initial = spark.createDataFrame(initial_data, schema=schema)

# Write DataFrame to Delta table
df_initial.write.format("delta").mode("overwrite").save(delta_table_path)

print("Initial Delta table created and data written successfully.")

# Define new sample data
new_sample_data = [
    (2, 250),  # Existing ID with updated Value
    (4, 400)   # New ID
]

# Create DataFrame for new data
df_new = spark.createDataFrame(new_sample_data, schema=schema)

# Write the new data to Delta table in append mode
df_new.write.format("delta").mode("append").save(delta_table_path)

print("New data appended to Delta table successfully.")

# Create a temporary view for SQL operations
df_new.createOrReplaceTempView("new_data")

# Perform the merge operation
print("Merging new data into Delta table...")

spark.sql(f"""
MERGE INTO delta.`{delta_table_path}` AS target
USING new_data AS source
ON target.ID = source.ID
WHEN MATCHED THEN UPDATE SET
    target.Value = source.Value
WHEN NOT MATCHED THEN INSERT (
    ID,
    Value
) VALUES (
    source.ID,
    source.Value
)
""")

print("Data merged successfully.")

# Delta operations - History, Time Travel, and Vacuum
print("Viewing Delta table history...")
history_df = spark.sql(f"DESCRIBE HISTORY delta.`{delta_table_path}`")
history_df.show(truncate=False)

print("Querying Delta table as of version 0...")
df_time_travel = spark.read.format("delta").option("versionAsOf", 0).load(delta_table_path)
df_time_travel.show(truncate=False)

print("Vacuuming old files...")
spark.sql(f"VACUUM delta.`{delta_table_path}` RETAIN 168 HOURS")

print("Delta operations completed.")
