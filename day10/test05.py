# 引用
# 1. int 不可变类型
a = 1
b = a
print(b)
print(id(a))
print(id(b))
a = 2
print(b)
print(id(a))
print(id(b))
print('='*50)
# 2. list 可变类型
aa = [1,2]
bb = aa
print(bb)
print(id(aa))
print(id(bb))
aa[0] = 100
print(bb)
print(id(aa))
print(id(bb))