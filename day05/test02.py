s = 'abcdefgh'
print(s[-1::-1])
print(s[::-1])
print(s[-4:-1:-1])  # 选取方向和步长方向需要一致才能取到数
print(f'c在的位置：{s.find("c")}')
