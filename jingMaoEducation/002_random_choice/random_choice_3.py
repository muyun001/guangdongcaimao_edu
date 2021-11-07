# 随机点名小程序
# 不会重复点到人
# 将文件持久化，放到txt中存储

import os
import random

"""
所有学生名单

被点名学生名单

未被点名名单
"""

"""
思路：
    1、程序创建all_students.txt/chosed_students.txt，分别用于存储"所有学生名单"、"被点名学生名单"
        1）如果文件已经存在，就无需创建
        2）如果文件不存在，就创建文件，并将"所有学生名单"写入到"all_students.txt"中
    2、读取两个txt文件，获取"所有学生名单"和"被点名学生名单"
    3、修改为：将"所有学生名单"和"已点名名单"取差集，得到所有"未点名名单"
    （3、从"所有学生名单"中随机点名，判断点到的名字是不是在"被点名学生名单"中
        1）如果在，重新点名，重新判断（函数嵌套）
        2）如果不在，就输出学生的名字，并把名字加到"chosed_students.txt"中）
    4、从"未点名名单"中随机点名，点名之后，把此名字从"未点名名单"中删除，并把名字添加到"chosed_students.txt"中
"""

# all_students_path = "./4班所有学生名单.txt"
# chosed_students_path = "./4班被点名名单.txt"

all_students_path = "./5班所有学生名单.txt"
chosed_students_path = "./5班被点名名单.txt"

# all_students_path = "./all_students.txt"
# chosed_students_path = "./chosed_students.txt"
all_students_list = list()  # 所有学生列表
chosed_students_list = list()  # 已经被点到的学生列表
remaining_students_list = list()  # 未被点到的学生列表
all_students_str = """"""



def file_exist():
    """
    判断"all_students.txt" 和 "chosed_students.txt" 文件是否存在，不存在就创建。
    """
    print("正在判断目标文件是否存在...")
    if not os.path.exists(all_students_path):
        with open(all_students_path, "w", encoding="utf-8") as f:
            f.writelines(all_students_str)
        print("目标文件{}不存在，已经成功创建并录入学生数据。".format(all_students_path))
    if not os.path.exists(chosed_students_path):
        file = open(chosed_students_path, "w", encoding="utf-8")
        file.close()
        print("目标文件{}不存在，已经成功创建。".format(chosed_students_path))


def read_students_list():
    """
    读取所有学生列表、被点名学生列表
    """
    print("开始读取学生列表...")

    global all_students_list, chosed_students_list
    with open(all_students_path, "r", encoding="utf-8") as f:
        all_students_list = [i.replace("\n", "") for i in f.readlines()]
    print("目前所有学生名单：", all_students_list)

    with open(chosed_students_path, "r", encoding="utf-8") as f:
        chosed_students_list = [j.replace("\n", "") for j in f.readlines()]
    print("目前已点名学生名单：", chosed_students_list)


def remaining_list():
    """
    使用列表差集的方法，获取未被点到的学生列表
    """
    global remaining_students_list
    remaining_students_list = list(set(all_students_list).difference(set(chosed_students_list)))


def random_choise(students):
    """
    随机选择学生名单
    :param students: 学生列表
    :return: 随机点到的人名
    """
    new_student = random.choice(students)
    print("\n新点到的学生为：【{}】\n".format(new_student))
    return new_student


# def random_choice():
#     """
#     从"目前未被点到的学生名单"中，随机点名
#     :return: student
#     """
#     return random.choice(remaining_students_list)


# def random_choice():
#     """
#     随机点名，并判断新选中的人是否在”已选中人名单列表中“
#         1）如果在，重新点名，重新判断（函数嵌套）
#         2）如果不在，就输出学生的名字，并把名字加到"chosed_students.txt"中
#     """
#     # 方法一：while循环
#     while True:
#         student = random.choice(all_students_list)
#         print("被点到的学生为：", student)
#         all_students_list.remove(student)  # 把名字从all_students_list中推出去
#         print("正在将{}")
#         if student not in chosed_students_list:
#             break
#     return student
#
#     # 方法二：嵌套函数
#     # student = random.choice(all_students_list)
#     # all_students_list.remove(student)  # 把名字从all_students_list中推出去
#     # if student in chosed_students_list:
#     #     random_choice()
#     # return student


def update_chosed_students(student):
    """
    更新chosed_students_list表和chosed_students.txt
    """
    # global remaining_students_list, chosed_students_list
    print('将"{}"写入到"已点名名单"中...'.format(student))
    chosed_students_list.append(student)
    with open(chosed_students_path, "a", encoding="utf-8") as f:
        f.write(student + "\n")
        print("写入成功")


def run():
    """
    开始运行
    """
    input("欢迎进入随机点名小程序！按任意键并回车即可开始运行。")

    # 判断"all_students.txt" 和 "chosed_students.txt" 文件是否存在，不存在就创建。
    file_exist()

    # 获取所有学生列表、被点名学生列表
    read_students_list()

    # 获取所有未被点名的学生列表
    remaining_list()

    while True:
        # 随机点名
        if not remaining_students_list:
            print("名单已点完，点名结束！")
            break

        print("目前未点名学生数量及名单：{}，{}".format(len(remaining_students_list), remaining_students_list))
        new_student = random_choise(remaining_students_list)
        # 将新点到的人名从"未点名名单"中去除掉
        remaining_students_list.remove(new_student)
        # 更新chosed_students_list表和chosed_students.txt
        update_chosed_students(new_student)

        input_str = input("\n-----按任意键回车可进行下一次随机点名，按q或Q回车可推出！-----\n")
        if input_str == "q" or input_str == "Q":
            break


# 入口函数
if __name__ == "__main__":
    run()
    # with open("./4班所有学生名单.txt", "r", encoding="utf-8") as f:
    #     # students = f.read()
    #     students = f.readlines()
    #     print(type(students))
    #     print(students)
