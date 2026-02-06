#1
nums = [5, 2, 9]
sorted_nums = sorted(nums, key=lambda x: x)
print(sorted_nums)
#2
words = ["banana", "fig", "apple"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)