"""
从系统中读取excel文件中的财贸学生数据，存储到mysql中
"""
import pymysql
import pandas as pd
import traceback

# 连接到数据库
connection = pymysql.connect(
    # host='106.12.154.238',  # 石老师服务器
    # host='172.16.125.144',  # 自己本地linux
    host='127.0.0.1',
    user='root',
    password='123456',
    database='caimao_students',
    charset='utf8'
)
cursor = connection.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
TABLE_NAME = "infos"


def read_s_info():
    """从excel中读取学生信息"""
    try:
        file_path4 = "/Users/muyun/Desktop/广东财贸相关资料/采集4班 - 学生绩效与就业详细信息.xlsx"
        file_path5 = "/Users/muyun/Desktop/广东财贸相关资料/采集5班 - 学生绩效与就业详细信息.xlsx"
        df4 = pd.read_excel(file_path4, sheet_name=0)  # sheet_name不指定时默认返回全表数据
        df5 = pd.read_excel(file_path5, sheet_name=0)  # sheet_name不指定时默认返回全表数据

        # 为了防止表格中为空，插入数据时报错，把dataframe中为nan的位置赋值为"无"
        df4.fillna("无", inplace=True)
        df5.fillna("无", inplace=True)

        # dataframe二维数据，series一维数据
        infos4 = df4.iloc[:, 0:10]  # 从dataframe中获取到series
        infos5 = df5.iloc[:, 0:10]  # 从dataframe中获取到series

        return infos4, infos5
    except:
        print("读取学生信息失败", traceback.print_exc())


def drop_photo(data4, data5):
    """删除dataframe中的照片"""
    return data4.drop(columns=["学生照片"]), data5.drop(columns=["学生照片"]),


def create_table():
    """创建表格"""
    create_sql = f"""
        create table if not exists `{TABLE_NAME}`(
            `id` INT UNSIGNED AUTO_INCREMENT comment "学号",
            `name` VARCHAR(16) NOT NULL comment "姓名",
            `class` VARCHAR(16) NOT NULL comment "班级",
            `group_name` varchar(16) not null comment "组名",
            `char` varchar(64) comment "性格情况",
            `want_job` varchar(16) comment "就业意向",
            `comm` varchar(128) comment "评语",
            `skill` varchar(16) comment "擅长技术",
            `talks` varchar(16) comment "谈话内容",
            PRIMARY KEY ( `id` )
        )
        """
    try:
        cursor.execute(create_sql)
        print("表格创建成功 / 表格已经存在无需创建")
    except:
        print("创建表格失败", traceback.print_exc())
        return -1


def insert_data(s_info):
    """mysql写入数据"""
    # insert into userInfo(name,password) values('ddf','8979'),('fsd','343'),('sf','45');
    # print([row for index, row in s_info.iterrows()])

    for index, row in s_info.iterrows():
        """
        'insert ignore into infos values(2019040257,"谢琼妹","大数据采集4班","山高组","外向、乐观开朗，感觉和任何人都能聊得来，很健谈。","沟通类工作。","她擅长体育，喜欢和人交谈，想从事沟通类的岗位。","无","2021-09-18谈话内容：性格、就业意向、擅长技术。")'
        """
        try:
            l = lambda s: f'"{s}"'.replace("\n", "").replace(",", "，") if isinstance(s, str) else s
            m = list(map(l, list(row)))
            rows = f'{m[0]},{",".join(m[1:])}'
            insert_sql = f"insert ignore into {TABLE_NAME} values({rows})"
            cursor.execute(insert_sql)
            connection.commit()
            print("插入数据成功！", list(row))
        except:
            print("插入数据报错", traceback.print_exc())
            print(row)
            return -1


if __name__ == '__main__':
    s_info4, s_info5 = drop_photo(*read_s_info())
    if create_table() == -1:
        print("创建表格失败，程序即将退出！")
        exit()

    if insert_data(s_info4) == -1:
        print("插入4班数据失败，程序即将退出！")
        exit()

    if insert_data(s_info5) == -1:
        print("插入5班数据失败，程序即将退出！")
        exit()

    cursor.close()
