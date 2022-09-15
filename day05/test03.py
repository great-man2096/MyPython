mystr = 'a b c b b c d b'
print(mystr.replace('b', 'f'))
print(mystr.replace(' ', '|'))
splited = mystr.split(' ', 5)
print(splited)
print(type(splited))

mylist = ['a', 'B', 'c']
joined = '\001'.join(mylist)
print(joined)
print(joined.capitalize())  # 首字母大写
print(joined.title())  # 所有单词首字母大写
print(joined.lower())  # 统一小写
print(joined.upper())  # 统一大写
print(mystr.strip())  # 输出首尾空白
