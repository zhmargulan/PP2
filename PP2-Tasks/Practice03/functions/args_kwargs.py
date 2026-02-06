#1
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
#2
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Bob", age=25)