def greet(name):
    return f"Hello,{name}!"

if __name__=="__main__":
    #This block will only run if this file is executed directly
    print("Executing mymodule as a script")
    name="world"
    print(greet(name))