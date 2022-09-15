from typing import Tuple

a: tuple[int, int, int, int] = (1,2,3,4)
s: str = '123456'
for x in a:
    print(x)
for y in s:
    if y == '3':
        print("遇到3不打印",end='')
        # break
        continue
    print(y, end='')
else:
    print('\n进入else',end='')