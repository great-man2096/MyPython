l1 = [1,2,3,4,5,6]
s1 = {1,2,3,4,5}
t1 = (1,2,3,4,5,6,7,1)
# 列表，集合，元组互相转换
print(tuple(l1))
print(tuple(s1))
print()
print(list(s1))
print(list(t1))
print('集合会自动去重：')
print(set(l1))
print(set(t1))