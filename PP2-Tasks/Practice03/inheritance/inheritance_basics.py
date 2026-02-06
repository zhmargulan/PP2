#1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass
#2
dog = Dog()
dog.speak()