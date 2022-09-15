import random

name_list = [['a', 'b', 'c'], ['1', '2', '3'], ['A', 'B', 'C']]
print(name_list[2][0])  # A

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

for i in teachers:
    x = random.randint(0, 2)
    offices[x].append(i)
else:
    print(offices)
j = 0
for i in offices:
    if len(i) == 0:
        print(f"{j}号有空教室")
    else:
        print(f"{j}号教室没问题啦")
    j += 1
