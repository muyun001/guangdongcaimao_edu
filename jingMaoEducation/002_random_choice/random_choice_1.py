# 随机选人的小程序
import random

students_str = """""".replace("    ", "")
students_list = students_str.split("\n")

input("欢迎进入随机选人小程序！按任意键开始运行。")
while True:
    student = random.choice(students_list)
    print("\n" + student + "\n")
    input_str = input("按任意键重新开始，按q(quit)回车退出！")
    if input_str == "q":
        break
