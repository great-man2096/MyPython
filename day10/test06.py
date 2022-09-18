def test(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))


i = 2
test(i)

j = [10, 20]
test(j)
