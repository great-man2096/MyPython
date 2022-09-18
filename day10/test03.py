# 位置参数
def user_info(a, b, c='默认值'):
    print(f'{a},{b},{c}')


user_info(1, 2, 3)
user_info(3, 2, 1)

# 关键字参数
user_info(c='c', b='b', a='a')


# user_info('c', b='b', a='a')  # 一个参数多个值会报错

# 组包
# 不定长参数，返回元组
def user_id2(*kwargs):
    print(kwargs)


user_id2(1, 2, 3)


# 包裹关键字传递,返回字典
def user_id(**kwargs):
    print(kwargs)


user_id(name='a', age=18, id=110)


# 拆包
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)
print(num2)
for i in enumerate(return_num(), start=1):
    print(i)

dict1 = {'name': 'a', 'age': 18, 'uid': 110}
name, age, uid = dict1
print(dict1[name].__eq__(dict1['name']))
print(dict1['name'])