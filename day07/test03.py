# 集合
s1 = set()  # 一个空集合
mySet = {9,1,1,2,3,4,4,5}  # 特性去重且无序，不支持下标
print(mySet)
s2 = set('adfgasdfgsdfg')
print(s2)
mySet.add(10)   # 追加单一数据
mySet.update([11,22,33])    # 追加多个数据需要序列
print(mySet)
mySet.remove(1)     # 删除不存在数据会报错
mySet.discard(6)    # 删除不报错
mySet.pop()         # 随机删除一个数并返回删除的数
print(mySet)
print(5 in mySet)