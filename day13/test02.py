f = open('test.txt', 'r')
line1 = f.readline()
print(line1,end='')
line2 = f.readline()
print(line2,end='')
f.close()