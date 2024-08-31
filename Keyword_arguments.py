def describe_pet(pet_name,animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}")
#using keyword arguments
describe_pet(animal_type="cat",pet_name="Whiskers")
describe_pet(pet_name="Rover")

