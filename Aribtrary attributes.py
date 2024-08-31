#tuple elements
def make_pizza(size, *toppings):
    print(f"making a{size}-inch pizza with the following topping")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(12,"Pepperoni","mushrooms","green peas")
# what are key words

#dictionary object
def build_profile(first,last,**user_info):
    return {"first_name":first,"last_name":last,**user_info}

#calling with arbitrary keyword arguments
user_profile=build_profile("John","Doe",location="New York",feild="Engineering")
print(user_profile)