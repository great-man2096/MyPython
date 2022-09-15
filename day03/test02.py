import random

flag = 0
while flag == 0:
    player = input("请输入石头剪刀布：")
    if player != "石头" and player != "剪刀" and player != "布" and player != "退出":
        print("请输入符合规范的字符：石头，剪刀，布或退出")
    elif player == "退出":
        exit("你已退出游戏")
    else:
        computer = random.randint(1, 3)

        if computer == 1:
            print("电脑使出了石头")
        elif computer == 2:
            print("电脑使出了剪刀")
        elif computer == 3:
            print("电脑使出了布")
        else:
            print("电脑出现故障")

        if (player == "石头" and computer == 2) or (player == "剪刀" and computer == 3) or (
                player == "布" and computer == 1):
            print("恭喜获胜！")
            flag = 1
        elif (player == "石头" and computer == 1) or (player == "剪刀" and computer == 2) or (
                player == "布" and computer == 3):
            print("平局")
        else:
            print("很遗憾，你输了！")
