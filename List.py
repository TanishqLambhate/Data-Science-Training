empty_list=[]
numbers=[1,2,3,4,5]
mixed_list=[1,"Hello",3.14,True]

print(empty_list)
print(numbers)
print(mixed_list)

fe=numbers[0]
se=numbers[2]
te=numbers[-1]
print(fe,se,te)

numbers[0]=10
print(numbers)#modify

numbers.append(6)
numbers.insert(2,2.5)
numbers.extend([7,8,9])
print(numbers)