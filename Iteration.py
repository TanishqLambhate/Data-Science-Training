from pprint import pprint

numbers=[1,2,3,4,5]

for num in numbers:
    print(num)

squares=[x**2 for x in range(6)]
print(squares)

person={
    "name":"Mark",
    "age":30,
    "email":"mark@example.com"

}

#Accessing values
name=person["name"]
age=person["age"]

print("Name:",name)
print("age",age)
#modifying values
person["age"]=31
person["email"]="mark_new@example.com"
print(person)

#Adding a new key-value pair
person["address"]="123 Main st"

#removing a key-value pair
del person["email"]

print(person)

keys=person.keys()
values=person.values()
items=person.items()

print("Keys:",keys)
print("values:",values)
print("Items:",items)

#Iterating over keys
for key in person:
    print(key)

# Iterating over values
for value in person.values():
    print(value)

#Iterating over keys
for key,value in person.items():
    print(key,":",value)