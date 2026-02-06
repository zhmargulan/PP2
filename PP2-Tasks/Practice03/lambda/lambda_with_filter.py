#1
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
#2
words = ["hi", "hello", "hey"]
long_words = list(filter(lambda w: len(w) > 2, words))
print(long_words)