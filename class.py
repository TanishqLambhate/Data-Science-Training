# self is the reference to curent class object
#Base class
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Animal Speaks")

ani=Animal("Bull")
ani.speak()