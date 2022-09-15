namelist = ['Tom', 'Lili', 'Wi']
del namelist[0]
print(namelist)

# pop() --删除指定下标数据，默认删最后一个，会返回被删除的数据
print(namelist.pop())
print(namelist)

namelist.remove('Lili')
print(namelist)

namelist.extend(['WoCao','LieKai'])
print(namelist)
namelist.clear()
print(namelist)