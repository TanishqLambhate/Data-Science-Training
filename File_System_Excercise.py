#
# ### JSON Exercises
#
# #### Exercise 1: Reading a JSON File
# 1. Create a JSON file named `data.json` with the following content:
#    ```json
#    {
#        "name": "John Doe",
#        "age": 30,
#        "city": "New York",
#        "skills": ["Python", "Machine Learning", "Data Analysis"]
#    }
#    ```
import json
data={
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Machine Learning", "Data Analysis"]
}
with open("C:/Users/Tanishq Lambhate/Documents/data.json","w") as file:
    json.dump(data,file)

# 2. Write a Python script to read and print the contents of the JSON file.

file_path = "C:/Users/Tanishq Lambhate/Documents/data.json"

with open(file_path, "r") as file:
    data = json.load(file)

print(data)

# #### Exercise 2: Writing to a JSON File
# 1. Create a Python dictionary representing a person's profile:
#    ```python
#    profile = {
#        "name": "Jane Smith",
#        "age": 28,
#        "city": "Los Angeles",
#        "hobbies": ["Photography", "Traveling", "Reading"]
#    }
#    ```
profile = {
    "name": "Jane Smith",
    "age": 28,
    "city": "Los Angeles",
    "hobbies": ["Photography", "Traveling", "Reading"]
}
# 2. Write a Python script to save this data to a JSON file named `profile.json`.

file_path = "C:/Users/Tanishq Lambhate/Documents/profile.json"

with open(file_path, "w") as file:
    json.dump(profile, file)


# #### Exercise 3: Converting CSV to JSON
# 1. Using the `students.csv` file from the CSV exercises, write a Python script to read the file and convert the data to a list of dictionaries.
# 2. Save the list of dictionaries to a JSON file called `students.json`.
import csv

csv_file_path = "C:/Users/Tanishq Lambhate/Documents/students.csv"

json_file_path = "C:/Users/Tanishq Lambhate/Documents/students.json"

students = []

with open(csv_file_path, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        students.append(row)

with open(json_file_path, mode="w") as json_file:
    json.dump(students, json_file)



# #### Exercise 4: Converting JSON to CSV
# 1. Using the `data.json` file from Exercise 1, write a Python script to read the JSON data.
# 2. Convert the JSON data to a CSV format and write it to a file named `data.csv`.


json_file_path = "C:/Users/Tanishq Lambhate/Documents/data.json"
csv_file_path = "C:/Users/Tanishq Lambhate/Documents/data.csv"

with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

with open(csv_file_path, mode="w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(data.keys())
    csv_writer.writerow(data.values())



# #### Exercise 5: Nested JSON Parsing
# 1. Create a JSON file named `books.json` with the following content:
#
books_data={
       "books": [
           {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
           {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
           {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
       ]
   }
with open("C:/Users/Tanishq Lambhate/Documents/books.json", "w") as json_file:
    json.dump(books_data,json_file)
# 2. Write a Python script to read the JSON file and print the title of each book.

with open("C:/Users/Tanishq Lambhate/Documents/books.json", "r") as json_file:
    data = json.load(json_file)

for book in data["books"]:
    print(book["title"])