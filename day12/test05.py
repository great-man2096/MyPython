import functools

# map
list1 = [1, 2, 3, 4, 5]
list2 = map(lambda x: x ** 2, list1)
print(list1)
print(list(list2))

# reduce
result = functools.reduce(lambda x, y: x + y, list1)
print(result)

# filter
filtered = filter(lambda x: x % 2 == 0, list1)
print(list(filtered))