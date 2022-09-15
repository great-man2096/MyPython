num1 = 1
num2 = 3.14159265

# 数据类型判断函数
typeName1 = type(num1)
typeName2 = type(num2)

# 输出数据类型
print(typeName1)
print(typeName2)

# str --- 字符类型
a = 'hello word !'
print(type(a))

# bool --- 布尔类型
b = True
print(type(b))

# list --- 列表
c = [1, 2, 3, 4]
print(type(c))
print(c[0])

# tuple --- 元组
d = (1, 2, 3, 4)
print(type(d))
print(d[0])

# set --- 集合
e = {1, 2, 3, 4}
print(type(e))
# print(e[0])

# dict --- 字典 --- 键值对
f = {'a': '1', 'b': 2, 'c': True}
print(type(f))
print(f.values())
