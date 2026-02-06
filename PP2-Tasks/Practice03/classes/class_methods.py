#1
class Math:
    @classmethod
    def add(cls, a, b):
        return a + b

print(Math.add(2, 3))
#2
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1