num_str="100"
num_int=int(num_str)

num_float=12.34
num_int_from_float=int(num_float)

print("string to integer",num_int)
print("float to integer",num_int_from_float)

x=10
y=5

#Comparison operators
is_greater=x>y #True
is_equal=x==y #False

print("x>y:", is_greater)
print("x == y:", is_equal)

################################################

a=True
b=False

#logical And

and_operation=a and b # a*b -- True * False --1*0 -- 0 - False

#Logical or
or_operation= a or b #True + False --True --1

#Logical Not
not_operation=not a #False

print("a and b:",and_operation)
print("a or b:",or_operation)
print("Not a:",not_operation)

#convert integer to bollean
bool_from_int=bool(1)#True

#convert zero to boolean
bool_from_zero=bool(0)#false

#convert string to boolean
bool_from_str=bool("Hello") #True

#convert empty string to boolean
bool_from_empty_str=bool("") #False

print("Boolean from integer 1:",bool_from_int)
print("Boolean from integer 0:",bool_from_zero)
print("Boolean from non empty string :",bool_from_str)
print("Boolean from empty string:",bool_from_empty_str)
