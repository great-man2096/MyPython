s = 'abcdefghaaaa'
print(s[-1::-1])
print(s[::-1])
print(s[-4:-1:-1])  # 选取方向和步长方向需要一致才能取到数
print(f'c在的位置：{s.find("c")}')
print(f'c在的位置(倒数)：{s.rfind("c")}')
print(f'c在的位置：{s.find("cba")}')
print(f'c在的位置：{s.find("a")}')

print(f'c在的位置：{s.index("a")}')
print(f'c在的位置(倒数)：{s.rindex("a")}')
# print(f'c在的位置：{s.index("cba")}')  # index查不到会报错

print(s.count('a'))
print(s.count("cba"))