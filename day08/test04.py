list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

for i in range(10):
    list1.append(i)
print(list1)

list2 = [i for i in range(15)]
print(list2)

list3 = [i for i in range(0, 10, 2)]
print(list3)
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)

list4 = [(i,j) for i in range(1,3) for j in range(3) if i % 2 == 0 and j % 2 == 0]
print(list4)