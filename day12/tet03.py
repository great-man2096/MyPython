df1 = lambda a, b: a if a > b else b
print(df1(1000,500))

students = [{'name':'Tom','age':18},{'name':'Rose','age':21},{'name':'Jack','age':20}]
students.sort(key=lambda x:x['name'])
print(students)
students.sort(key=lambda x:x['age'])
print(students)

list1 = [10,8,3,4,6,9]
list1.sort(reverse=True)
print(list1)