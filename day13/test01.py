# f = open('test.txt', 'w')
# f = open('test.txt', 'a')
f = open('test.txt', 'r')
# f.write('wocao')
# print(f.read())

lines = f.readlines()
for i in lines:
    print(i,end='')
f.close()
