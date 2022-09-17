def avg_input_num(*x:int) -> float:
    print(sum(x))
    print(len(x))
    return sum(x)/len(x)


result = avg_input_num(1,2,3,4)
print('%d' % result)
