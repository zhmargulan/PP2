from datetime import datetime

# 1 Generator that generates squares up to N
def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i


# 2 Generator for even numbers up to n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# 3 Generator for numbers divisible by 3 and 4 up to n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# 4 Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


# 5 Countdown generator from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# ================== TESTING ==================

n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("\n1 Squares up to n:")
for num in squares_up_to_n(n):
    print(num, end=" ")

print("\n\n2 Even numbers up to n (comma separated):")
print(",".join(str(num) for num in even_numbers(n)))

print("\n\n3 Numbers divisible by 3 and 4 up to n:")
for num in divisible_by_3_and_4(n):
    print(num, end=" ")

print("\n\n4 Squares from a to b:")
for value in squares(a, b):
    print(value, end=" ")

print("\n\n5 Countdown from n to 0:")
for number in countdown(n):
    print(number, end=" ")
