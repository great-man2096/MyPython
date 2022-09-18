def test1():
    return 50,60


def test2(n):
    print(n)
    for i in n:
        print(i)


test2(test1())
