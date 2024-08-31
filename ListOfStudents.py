students=[
    {"name":"Alice","age":20,"grade":"A"},
    {"name":"Bob","age":22,"grade":"B"},
    {"name":"Charlie","age":21,"grade":"C"},
    {"name":"David","age":23,"grade":"B"},
]

#Accessing and manipulating  individual records
print(students[0]["name"]) #Accessing the name of the first student
students[1]["age"]=24

#Adding a new student record to the list
new_student={"name":"Eva","age":19,"grade":"A"}
students.append(new_student)

for student in students:
    print(f"Name:{student['name']},Age:{student['age']},Grade:{student['grade']}")

