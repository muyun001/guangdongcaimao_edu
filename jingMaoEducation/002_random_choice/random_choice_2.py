# 随机选人的小程序
# 不会重复点到人
import random


def read_student_info():
    """
    读取学生信息
    :return: student_list
    """
    students_str = """黎秋霞
    蓝小龙
    周鸿成
    麦泽楷
    陈源斌
    罗小平
    钟景昊
    朱家润
    杨文龙
    陈昌
    陈兴源
    辜灿扬
    何燕琳
    徐茜
    叶子洋
    莫俊青
    李如力
    龙作森
    黎青华
    钟伟昌
    钟国鹏
    严有水
    王昌栋
    董海权
    罗世宝
    吴海锋
    彭泽昕
    吴文敏
    张嘉敏
    林港杰
    柯永铭
    李湛
    裴志勇
    刘梓彬
    赖建均
    黄幸浩
    黄燕凤
    李依婷
    倪世杰
    陈开富
    蔡树涛
    梁发亮
    许小林
    陈伟贤
    莫介超""".replace("    ", "")
    return students_str.split("\n")


def random_choice(students):
    """
    随机选出一个人
    :param students:
    :return: 随机选出来的一个人
    """
    return random.choice(students)


def random_print(students_list):
    """
    随机打印学生信息
    """
    chosed_student = list()  # 已经选中的人
    input("欢迎进入随机选人小程序！按任意键开始运行。")
    while True:
        student = random_choice(students_list)
        if student not in chosed_student:  # 新选中的人不在”已选中人名单列表中“
            chosed_student.append(student)  # 将新人添加到列表中
            print("\n" + student + "\n")
            print("chosed_student:", chosed_student)
            input_str = input("按任意键重新开始，按q(quit)回车退出！")
            if input_str == "q":
                break


if __name__ == "__main__":
    student_list = read_student_info()
    random_print(student_list)
