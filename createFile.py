#specify the file path name
file_path="C:/Users/Tanishq Lambhate/Documents/example.txt"

#open the file in write mode and write content
with open(file_path,"w") as file:
    file.write("Hello, this is content written "
               "to a file in ur Laptop!!!")

print("File created and content written successfully")

#open a file in read mode and print each line
with open("C:/Users/Tanishq Lambhate/Documents/example.txt","r") as file:
    for line in file:
        print(line.strip()) #Remove newline characters /n

# Open a file in append mode and add new content
with open("C:/Users/Tanishq Lambhate/Documents/example.txt","a") as file:
    file.write("\n This is additional content appended to the file.")

with open("C:/Users/Tanishq Lambhate/Documents/example.txt","r") as file:
    content=file.read()
    print(content)

import csv
#writing data to a csv file
data=[["Name","age"],["Alice",25],["Bob",30]]
with open("C:/Users/Tanishq Lambhate/Documents/data.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(data)

with open("C:/Users/Tanishq Lambhate/Documents/students.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(data)

## Reading data from a csv file
with open("C:/Users/Tanishq Lambhate/Documents/data.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

import json
#writing data to a json file
with open("C:/Users/Tanishq Lambhate/Documents/data.json","w")as file:
    json.dump(data,file)

#Reading data from a JSON file
with open("C:/Users/Tanishq Lambhate/Documents/data.json","r") as file:
    loaded_data=json.load(file)
    print(loaded_data)