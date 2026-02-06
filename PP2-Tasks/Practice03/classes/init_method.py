#1
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)
#2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year