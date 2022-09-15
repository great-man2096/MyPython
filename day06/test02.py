namelist = ['Tom','Lili','Wi']
name = input("请输入注册用户名：")
flag = True
while flag:
    if name in namelist:
        name = input(f"您输入的用户名{name}已存在，请重输：")
    else:
        flag = False
        print(f'用户名正常,将用户{name}添加至列表首位')
        # namelist.append(name)
        namelist.insert(0,name)
print(f'''用户列表如下：
            {namelist}''')