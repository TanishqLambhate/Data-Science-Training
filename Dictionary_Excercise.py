#
# ### Exercise 1: Create a Dictionary
# 1. Create a dictionary called `person` with the following key-value pairs:
#    - Name: "Alice"
#    - Age: 25
#    - City: "New York"
# 2. Print the dictionary.

person={
    "Name":"Alice",
    "Age":25,
    "City":"New York"
}
print(person)

# ### Exercise 2: Access Dictionary Elements
# C.
# 2. Access the value of the `"City"` key and print it.

city=person["City"]
print(city)

# ### Exercise 3: Add and Modify Elements
# 1. Add a new key-value pair to the `person` dictionary: `"email": "alice@example.com"`.
# 2. Change the value of the `"Age"` key to 26.
# 3. Print the modified dictionary.

person["email"]="alice@example.com"
person["Age"]=26
print(person)

# ### Exercise 4: Remove Elements
# 1. Remove the `"City"` key from the `person` dictionary.
# 2. Print the dictionary after removing the key.

del person["City"]
print(person)

# ### Exercise 5: Check if a Key Exists
# 1. Check if the key `"email"` exists in the `person` dictionary. Print a message based on the result.
# 2. Check if the key `"phone"` exists in the dictionary. Print a message based on the result.

if "email" in person:
    print("The key 'email' exists in the dictionary.")
else:
    print("The key 'email' does not exists in the dictionary.")
if "phone" in person:
    print("The key 'phone' exists in the dictionary.")
else:
    print("The key 'phone' does not exists in the dictionary.")


# ### Exercise 6: Loop Through a Dictionary
# 1. Iterate over the `person` dictionary and print each key-value pair.
# 2. Iterate over the keys of the dictionary and print each key.
# 3. Iterate over the values of the dictionary and print each value.

for k,v in person.items():
    print(k,":",v)

for k in person.keys():
    print(k)

for v in person.values():
    print(v)

# ### Exercise 7: Nested Dictionary
# 1. Create a dictionary called `employees` where the keys are employee IDs (`101`, `102`, `103`) and the values are dictionaries containing employee details (like name and job title). Example structure:
#    ```python
#    employees = {
#        101: {"name": "Bob", "job": "Engineer"},
#        102: {"name": "Sue", "job": "Designer"},
#        103: {"name": "Tom", "job": "Manager"}
#    }
#    ```

employees = {
       101: {"name": "Bob", "job": "Engineer"},
       102: {"name": "Sue", "job": "Designer"},
       103: {"name": "Tom", "job": "Manager"}
   }

# 2. Print the details of employee with ID `102`.
emp102=employees[102]
print(emp102)
# 3. Add a new employee with ID `104`, name `"Linda"`, and job `"HR"`.
employees[104]={"name": "Linda", "job": "HR"}
# 4. Print the updated dictionary.
print(employees)
# ### Exercise 8: Dictionary Comprehension
# 1. Create a dictionary comprehension that generates a dictionary where the keys are numbers from 1 to 5 and the values are the squares of the keys.
# 2. Print the generated dictionary.

squared={i**2 for i in range(1,6)}
print(squared)

# ### Exercise 9: Merge Two Dictionaries
# 1. Create two dictionaries:
#    ```python
#    dict1 = {"a": 1, "b": 2}
#    dict2 = {"c": 3, "d": 4}
#  ```

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# 2. Merge `dict2` into `dict1` and print the result.
dictionary={**dict1,**dict2}
print(dictionary)
# ### Exercise 10: Default Dictionary Values
# 1. Create a dictionary that maps letters to numbers: `{"a": 1, "b": 2, "c": 3}`.

letters_to_numbers = {"a": 1, "b": 2, "c": 3}

# 2. Use the `get()` method to retrieve the value of key `"b"`.

print(letters_to_numbers.get("b"))

# 3. Use the `get()` method to try to retrieve the value of a non-existing key `"d"`, but provide a default value of `0` if the key is not found.

print(letters_to_numbers.get("d", 0))

# ### Exercise 11: Dictionary from Two Lists
# 1. Given two lists:
keys = ["name", "age", "city"]
values = ["Eve", 29, "San Francisco"]

# 2. Create a dictionary by pairing corresponding elements from the `keys` and `values` lists.
combined_dict = dict(zip(keys, values))
print(combined_dict)

# 3. Print the resulting dictionary.
print(combined_dict)

# ### Exercise 12: Count Occurrences of Words
# 1. Write a Python program that takes a sentence as input and returns a dictionary that counts the occurrences of each word in the sentence.
#    ```python
#    sentence = "the quick brown fox jumps over the lazy dog the fox"
#    ```
sentence = "the quick brown fox jumps over the lazy dog the fox"
splitted=sentence.split()
print(splitted)
occurences={}
for word in splitted:
    occurences[word]=splitted.count(word)

# 2. Print the dictionary showing word counts.
print(occurences)
