# lambda表达式
df2 = lambda a,b:a+b
print(df2(1,2))

df3 = lambda a,b,c=10:a+b+c
print(df3(0,b=20))

df4 = lambda *args:args
print(df4(1,2,3))

df5 = lambda **kwargs:kwargs
print(df5(a=1,b=2,c=3))