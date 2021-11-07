import pandas as pd


def namestr(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj and len(name) > 1]  # 定义函数


student_name = pd.DataFrame({"学号": [1, 2, 3, 4, 5], "姓名": ["赵", "钱", "孙", "李", "周"]})
student_info = pd.DataFrame({"姓名": ["赵", "钱", "孙", "李", "周"], "性别": ["男", "女", "女", "男", "女"]})

sheets = [student_name, student_info]  # 表格列表
names = []  # 表名列表

for sheet in sheets:  # 将表名添加到表名列表
    names.append(namestr(sheet)[0])
