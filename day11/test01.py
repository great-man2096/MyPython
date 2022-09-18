def info_print():
    print("""==================================
    请输入序号以选择功能：
    1、添加学员
    2、删除学员
    3、修改学员信息
    4、查询学员信息
    5、显示所有学员信息
    6、退出系统
=====================================""")


def add_info():
    """新增学员"""
    name = input("请输入要新增的学员：")
    uid = len(stu_infos)
    is_not_exit = True
    for i in stu_infos:
        if i['name'] == name:
            is_not_exit = False
    if is_not_exit:
        stu_infos.append({'uid': uid, 'name': name})
    else:
        print("该用户已经存在，无法新增")


def del_info():
    """删除学员"""
    name = input("请输入要删除的学员：")
    is_exit = False
    for i in stu_infos:
        if i['name'] == name:
            stu_infos.remove(i)
            is_exit = True
    if is_exit:
        print(f"已删除学员{name}")
    else:
        print("该学员不存在")


def up_info():
    """修改学员"""
    name = input("请输入要修改的学员：")
    is_not_exit = True
    for i in stu_infos:
        if i['name'] == name:
            is_not_exit = False
            i['uid'] = input("修改他的学号")
    if is_not_exit:
        print("该学员不存在")


def sel_info():
    """查询指定学员"""
    name = input("请输入要查询的学员：")
    for i in stu_infos:
        if i['name'] == name:
            print(i)
    else:
        print("该学员不存在")


flag = True
stu_infos = []
while flag:
    info_print()
    input_num = int(input())

    if input_num == 1:
        add_info()
    elif input_num == 2:
        del_info()
    elif input_num == 3:
        up_info()
    elif input_num == 4:
        sel_info()
    elif input_num == 5:
        print("显示所有学员信息:")
        for i in stu_infos:
            print(i)
    elif input_num == 6:
        print("退出系统!")
        flag = False
    else:
        print("您输入的序号有误，请重新输入")
