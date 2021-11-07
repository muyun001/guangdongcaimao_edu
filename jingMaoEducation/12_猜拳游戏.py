# 猜拳游戏
"""
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负
"""
# import random
#
# print(random.randint(0, 3))  # 随机输出1～3之间的整数值

#  刚开始先设置电脑指出石头（1）

# if 电脑赢：
# print("不行，我要和你决战到天亮！")
# elif 我赢：
# print("噢耶！！！电脑弱爆了！！！")
# else:  # 平局
# print("心有灵犀，再来一盘！")
#
# if 平局：
# print("心有灵犀，再来一盘！")
# elif 电脑赢：
# print("不行，我要和你决战到天亮！")
# else:
# print("噢耶！！！电脑弱爆了！！！")

"""
需求：
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负

# 需求拆解：
1、玩家的输入值
2、电脑的值 1（石头）
3、进行比较
"""
import random

# 1、获取玩家的值
player = int(input("玩家请输入：石头（1）／剪刀（2）／布（3）"))
# 2、获取电脑值
computer = random.randint(1, 3)
print("computer:", computer)

# 进行比较

# 玩家赢：
# 电脑=1，玩家=3
# 电脑=2，玩家=1
# 电脑=3，玩家=2

# 电脑赢
# 电脑=1，玩家=2
# 电脑=2，玩家=3
# 电脑=3，玩家=1

if (computer == 1 and player == 3) or \
        (computer == 2 and player == 1) or \
        (computer == 3 and player == 2):  # 玩家赢
    print("噢耶！！！电脑弱爆了！！！")
elif (computer == 1 and player == 2) or \
        (computer == 2 and player == 3) or \
        (computer == 3 and player == 1):  # 电脑赢
    print("不行，我要和你决战到天亮！")
else:  # 平局
    print("心有灵犀，再来一盘！")
