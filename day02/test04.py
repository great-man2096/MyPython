age = eval(input("请输入您的年龄："))
if age > 18:
    print(f'{age}岁yes')
elif age == 18:
    print(f'刚好{age}岁')
else:
    print(f'{age}岁no')
print("系统关闭")