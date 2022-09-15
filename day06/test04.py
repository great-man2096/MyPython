namelist = ['0',1, 2, 3,4]
namelist[0] = 0

print(namelist[::-1])  # 只做了变化，没有改变序列结构
namelist.reverse()
print(namelist)

namelist.sort(reverse=False)  # 升序排序,reverse不写默认False
print(namelist)

namelist.sort(reverse=True)  # 降序排序
print(namelist)

namelist2 = namelist.copy()  # 复制序列
print(namelist2)