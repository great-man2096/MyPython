t1 = ('a','b','c',[1,2,3,4])
print(len(t1))
print(t1[1])
print(t1.index('c'))
print(t1.count('b'))
print(t1.count('d'))
t1[-1][0] = 0
print(t1)