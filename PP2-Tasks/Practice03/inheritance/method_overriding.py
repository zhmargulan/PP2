class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")
p = Penguin()
p.fly()