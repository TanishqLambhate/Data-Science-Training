# Exercise 1: Create a List
# Create a list called fruits with the following items: "apple", "banana", "cherry", "date", and "elderberry".
# Print the list.


Fruits=["apple", "banana", "cherry", "date","elderberry"]
print(Fruits)

# Exercise 2: Access List Elements
# Print the first and last items from the fruits list.
# Print the second and fourth items from the list.

first_element=Fruits[0]
last_elements=Fruits[-1]
print(first_element)
print(last_elements)

# Exercise 3: Modify a List
# Replace "banana" in the fruits list with "blueberry".
# Print the modified list.

Fruits[1]="blueberry"
print(Fruits)

# Exercise 4: Add and Remove Elements
# Append "fig" and "grape" to the fruits list.
# Remove "apple" from the list.
# Print the final list.

Fruits.append("fig")
Fruits.append("grape")
Fruits.remove("apple")
print(Fruits)

# Exercise 5: Slice a List
# Slice the first three elements from the fruits list and assign them to a new list called first_three_fruits.
# Print first_three_fruits.

first_three_fruits=Fruits[:3]
print(first_three_fruits)

# Exercise 6: Find List Length
# Find and print the length of the fruits list.

length=len(Fruits)
print(length)

# Exercise 7: List Concatenation
# Create a second list called vegetables with the following items: "carrot", "broccoli", "spinach".
# Concatenate the fruits and vegetables lists into a new list called food.
# Print the food list.

Vegetables=["carrot", "broccoli", "spinach"]
Food=Fruits+Vegetables
print(Food)


# Exercise 8: Loop Through a List
# Loop through the fruits list and print each item on a new line.

for fruit in Fruits:
    print(fruit)

# Exercise 9: Check for Membership
# Check if "cherry" and "mango" are in the fruits list. Print a message for each check.

if "cherry" in Fruits:
    print("Cherry is in Fruits")
else:
    print("Cherry not present in Fruits")
if "mango" in Fruits:
    print("mango is in Fruits")
else:
    print("mango not present in Fruits")

# Exercise 10: List Comprehension
# Use list comprehension to create a new list called fruit_lengths that contains the lengths of each item in the fruits list.
# Print the fruit_lengths list.

fruit_lengths=[len(fruit) for fruit in Fruits]
print(fruit_lengths)

# Exercise 11: Sort a List
# Sort the fruits list in alphabetical order and print it.
# Sort the fruits list in reverse alphabetical order and print it.

Fruits.sort()
print("fruits list in alphabetical order",Fruits)

Fruits.sort(reverse=True)
print("fruits list in reverse alphabetical order",Fruits)

# Exercise 12: Nested Lists
# Create a list called nested_list that contains two lists: one with the first three fruits and one with the last three fruits.
# Access the first element of the second list inside nested_list and print it.

nested_list=[Fruits[:3],Fruits[-3:]]
print(nested_list[1][0])

# Exercise 13: Remove Duplicates
# Create a list called numbers with the following elements: [1, 2, 2, 3, 4, 4, 4, 5].
# Remove the duplicates from the list and print the list of unique numbers.

Numbers=[1,2,2,3,4,4,4,5]
unique_number=[]
for num in Numbers:
    if num not in unique_number:
        unique_number.append(num)

print(unique_number)

# Exercise 14: Split and Join Strings
# Split the string "hello, world, python, programming" into a list called words using the comma as a delimiter.
# Join the words list back into a string using a space as the separator and print it.

string= "hello, world, python, programming"
comma_seperated=string.split(",")
print(comma_seperated)
joined_string=" ".join(comma_seperated)
print(joined_string)

