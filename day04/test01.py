flag: bool = True
i: int = 0
s: int = 0
while flag:
    s = s + i
    i += 2

    if i == 102:
        break
        # flag = False

print(s)