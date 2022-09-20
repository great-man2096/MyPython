# 递归
def test01(num):
    if num != 1:
        return num + test01(num - 1)
    else:
        return 1


result = test01(3)
print(result)
