mylist = ['1', 'a', '1.2', True]
l = 0
for i in mylist:
    if l == 3:
        continue
    print(i)
    l += 1
else:
    print("δΌιη»ζ")

print(mylist.index(True))
print(mylist.count(False))
print(len(mylist))
print('1' in mylist)
print('2' not in mylist)