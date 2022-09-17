# 函数
def myFunction(a, b):
    """
    :param a: 基数
    :param b: 指数
    :return: a的b次方
    """
    return a ** b


def antherFunction():
    """嵌套调用"""
    for i in range(10):
        j = 2
        print(myFunction(i, j))
    else:
        help(myFunction)


antherFunction()
