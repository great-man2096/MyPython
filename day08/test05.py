list1 = ['name', 'age', 'gender']
list2 = ['Tom', '23', 'man', '']

dict1 = {list1[i]: list2[i] for i in range(len(list1))}  # 统计多的会报错，因为匹配不到空的
print(dict1)

dict2 = {i: i ** 2 for i in range(5)}
print(dict2)

counts = {'a': 268, 'b': 125, 'c': 201, 'd': 199, 'e': 99}
dictResult = {k: v for k, v in counts.items() if v >= 200}
print(dictResult)

list3 = {1, 1, 2}
list3 = {i ** 2 for i in list3}
print(list3)
