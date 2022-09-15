mystr = 'a b c b b c d b'
print(mystr.startswith('a'))  # 是否以a开头
print(mystr.endswith('b'))  # 是否以b结尾
print()
mystr2 = '123456'
print(mystr.isalpha())  # 是否纯字母
print(mystr2.isalnum())  # 是否纯字母数据组合
print(mystr2.isdigit())  # 是否纯数字
print(mystr.isspace())  # 是否是纯空格
print(' ' in mystr)  # 是否有空格