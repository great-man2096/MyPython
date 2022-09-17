# 字典
zidian = {'a':1,'b':{'A':11,'B':22},'c':3}
print(zidian.keys())
for i in zidian.keys():
    print(i)
print(zidian.values())
print(zidian['b']['B'])
print(zidian.get('d', -1))   # 如果查不到则返回传入的第二个参数,默认值是None
print(zidian.items())   # 转换成元组
for x in zidian.items():
    print({type(x)})
    print(x)
for i,j in zidian.items():
    print(f'{i}:{j}')
zidian['b']['B'] = 00   # 如果存在则覆盖
zidian['b']['C'] = 33   # 如果不存在则新增
del zidian['c']  # 如果k值不存在则会报错
zidian.clear()  # 清空
print(zidian)
dict2 = {}
dict3 = dict()
print(type(zidian))
print(type(dict2))
print(type(dict3))
