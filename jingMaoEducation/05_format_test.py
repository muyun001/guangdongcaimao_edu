# format()函数

# print("我的电话是：{}，我的邮箱是{}".format(123456779.0, "1111111@qq.com"))
print(("我的姓名：{name}，公司：{company}，职位：{job}，电话：{number}，邮箱：{email}"
       .format(name="张三", company="联想教育", job="讲师", number=123467869, email="112312312@qq.com")))

# info_dict = {"name": "张三", "gender": "男", "age": 18, "hobby": "羽毛球"}
# print("我的基础信息：姓名：{name}，性别：{gender}，年龄：{age}，爱好：{hobby}".format(**info_dict))

# print(**info_dict)


sss = "网站名：{}, 年龄 {}".format("张三", 19)
print("网站名：{name}, 年龄 {age}".format(name="张三", age=19))

# format()函数中冒号（：）的使用
# 精确到小数点后几位
s = 3.141592654
print("{:.2f}".format(s))  # 3.14

# 自动补0
ss = "{:03d}".format(1)
print(ss)

############3

# format()函数
print("姓名：%s,年龄：%s" % ("张三", 19))
print("姓名：{},年龄：{}".format("张三", 19))
print("姓名：{aaaa},年龄：{vvvv}".format(vvvv=19, aaaa="张三"))

# 自动补0
ss = "{:06d}".format(2)
print(ss)
print(len(ss))

# format()格式化
print("姓名：%s,年龄：%s" % ("zyangsan", 19))
print("姓名：{},年龄：{}".format("zhangsan", 19))
print("姓名：{name},年龄：{age}".format(age=19, name="zhangsan"))
# 姓名：zhangsan,年龄：19

# print(("我的姓名：{name}，公司：{company}，职位：{job}，电话：{number}，邮箱：{email}"
#        .format(name="张三", company="联想教育", job="讲师", number=123467869, email="112312312@qq.com")))


# 精确到小数点后几位
s = 3.141592654
print("{:.4f}".format(s))  # 3.1416

# 自动补0
sss = "{age:03d}".format(age=30)
# print(sss)  # 2   # 002
# print(len(sss))  # 3

# 占位符和制表符

# 占位符使用场景，比如函数中传参
def print_student_info(name, age):
    """
    输出学生信息
    """
    student_info = "学生信息是：姓名：%s，年龄：%s" % (name, age)
    print(student_info)


print_student_info("张三", 18)
print_student_info("李四", 19)

# 制表符
# print("学号\t姓名\t语文\t数学\t英语")
# print("2019001\t曹操\t99\t88\t0")

print("vaaabbbbbba\rm")

# %10d 表示输出的整数宽度至少为 10
# %20s 表示输出的字符串宽度至少为 20
# %06d，不够6位数就补0，同理：%016d，不够16位就补0
student_no = 1
print("我的学号是 %06d" % student_no)  # 我的学号是 000001
print("我的学号是 %016d" % student_no)  # 我的学号是 000001
print(len("%16d" % student_no))  # 我的学号是 000001

scale = 0.2
print("数据比例是 %.02f%%" % (scale * 100))  # 数据比例是20.00%

# format控制宽度
age = 25
name = 'Caroline'
print('{0} is {1} years old. '.format(name, age))  # 输出参数
print('{0} is a girl. '.format(name))
print('{0:.3} is a decimal. '.format(1 / 3))  # 小数点后三位   # 0.333 is a decimal.
print('{0:_^11} is a 11 length. '.format(name))  # 使用_补齐空位
print('{first} is as {second}. '.format(first=name, second='Wendy'))  # 别名替换
print('My name is {0.name}'.format(open('out.txt', 'w')))  # 调用方法
print('My name is {0:8}.'.format('Fred'))  # 指定宽度


print("ip地址是：%s" % (192))
print("ip地址是：{}".format(192))
print("ip地址是：{ip}".format(ip=192))
print(f"ip地址是:{192}")
