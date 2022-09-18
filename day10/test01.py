
a = 0


def testA():
    global a  # 声明a是全局变量
    a = 1
    print(a)


testA()
print(a)
