# 石头剪刀布
import random

computer_choice = [2]

input("按任意键开始游戏")
while True:
    player = int(input("请出拳 石头（1）/ 剪刀（2）/ 布（3）"))
    if player == "":
        print("输入为空，请重新输入！")
        continue
    computer = random.choice(computer_choice)
    print(computer)

    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):
        print("电脑弱爆了！")
    elif player == computer:
        print("心有灵犀，再来一盘！")
    else:
        print("不行，再战三百回合！")
    input_str = input("继续游戏 \n(输入q退出):")
    if input_str == "q":
        break

import subprocess