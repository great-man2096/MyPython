def print_line(x):
    return '-' * x


def print_lines(j):
    for i in range(1, j + 1):
        # print(i)
        print(print_line(i))


print_lines(5)
