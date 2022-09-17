for i in range(1,10,2):     # 三个参数：start[,stop),step
    print(i)
for i in range(10):     # 默认start=0,step=1
    print(i)

list1 = ['a','b','c','d']
for i in enumerate(list1,start=1):  # 返回元组，且设置起始值为1.不设置默认为0
    print(i)