class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog=Dog("Buddy")
cat=Cat("Whiskers")

# Creating instances of derived classes
dog=Dog("Buddy")
print(f"{dog.name} says:{dog.speak()}")
print(f"{cat.name} says:{cat.speak()}")

class Payment:
    def __init__(self):
        pass
    def getPayment(self):
        pass
class GPay(Payment):
    def getPayment(self):
        print("Speaking Google Payment")
class PhonePay(Payment):
    def getPayment(self):
        print("Speaking PhonePe Payment")
class AmazonPay(Payment):
    def getPayment(self):
        print("Speaking Amazon Payment")

gpay=GPay()
print(gpay.getPayment())
phonepe=PhonePay()
print((phonepe.getPayment()))

