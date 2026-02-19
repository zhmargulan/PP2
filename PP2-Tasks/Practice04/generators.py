#1
def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i

# Example
for num in squares_up_to_n(5):
    print(num)
#2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))

print(",".join(str(num) for num in even_numbers(n)))
#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Test
for value in squares(3, 7):
    print(value)
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example
for number in countdown(5):
    print(number)
