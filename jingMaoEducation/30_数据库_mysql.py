import pymysql
import traceback

# 连接到数据库
connection = pymysql.connect(
    # host='106.12.154.238',
    host='127.0.0.1',
    user='root',
    password='123456',
    database='test',
    charset='utf8'
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = connection.cursor()
table_name = "students"


def create_table():
    """创建表格"""
    create_sql = f"""create table if not exists `{table_name}`(
            `id` INT UNSIGNED AUTO_INCREMENT comment "学号",
            `name` VARCHAR(16) NOT NULL comment "姓名",
            `class` VARCHAR(16) NOT NULL comment "班级",
            `group_name` varchar(16) not null comment "组名",
            `char` varchar(64) comment "性格情况",
            `want_job` varchar(16) comment "就业意向",
            `comm` varchar(128) comment "评语",
            `skill` varchar(16) comment "擅长技术",
            `talks` varchar(64) comment "谈话内容",
            PRIMARY KEY ( `id` ))"""
    try:
        cursor.execute(create_sql)
        print("表格创建成功 / 表格已经存在无需创建")
    except:
        traceback.print_exc()
        return -1


def insert_table():
    """插入数据"""
    """
    数据举例：
    'insert ignore into students values(2019040257,"谢琼妹","大数据采集4班","山高组","外向、乐观开朗，感觉和任何人都能聊得来，很健谈。","沟通类工作。","她擅长体育，喜欢和人交谈，想从事沟通类的岗位。","无","2021-09-18谈话内容：性格、就业意向、擅长技术。")'
    'insert ignore into students values(2019040434,"林文旭","大数据采集4班","山高组","开朗，有上进心，有想法并能付诸实践。","想从事本专业相关工作，但具体哪个方向还没考虑好。","底子好，也很认真的学习，报过几个课程或考试，如web前端、国家计算机2级、网络工程师、数据库工程师。并于近期会参加前端考试。并且之前暑假的时候就想找过这方面实习。","web、mysql","2021-09-18谈话内容：性格、就业意向、擅长技术、以及对自己未来的规划。")'
    'insert ignore into students values(2019040441,"胡志超","大数据采集4班","山高组","内向","前端、python","python基础还行，其他课程如mysql、linux都忘的差不多了。","python","2021-09-18谈话内容：性格、就业意向、擅长技术。")'
    'insert ignore into students values(2019040438,"蒋家宝","大数据采集4班","山高组","之前外向，现在内向，腼腆。","没想过","很腼腆，不过人很好，布置的作业都能完成。希望能好好引导一下，让他有一些危机意识，早些为工作做准备。","无","2021-09-18谈话内容：性格、就业意向、擅长技术、兴趣爱好，以及毕业前对规划。并提醒他提前做好找工作对准备。")'
    'insert ignore into students values(2019040207,"郑榕彬","大数据采集4班","山高组","偏内向，肯吃苦，之前不自信，现在好很多了。脾气不稳定","本专业相关工作优先","挺腼腆的人，想找本专业的工作，但是明显没信心。","无","2021-10-8谈话内容：近期学习情况、性格、就业意向、擅长技术，以及短期规划。")'
    'insert ignore into students values(2019040244,"林煊骤","大数据采集4班","山高组","偏内向，随和，熟人聊的来","想毕业后参军","想在毕业后参军，来学校之前就已经体检过了，由于学校方面原因没去成。并且退伍后想去继续读本科。学习态度比较好，作业基本上可以独立完成。","无","2021/09/29谈话内容：近期学习情况、性格、就业意向、擅长技术，以及短期规划。")'
    'insert ignore into students values(2019040225,"杨晓澎","大数据采集4班","山高组","乐观，开朗","本专业相关工作","学习状态很好，自学过爬虫，也经常是优秀日报上榜者。","web、python","2021/10/13谈话内容：近期学习情况、性格、就业意向、擅长技术，以及短期规划。")'
    'insert ignore into students values(2019040419,"林道友","大数据采集4班","山高组","性格外向，喜欢交流","在考虑是做生意还是就业","现在手里有创业项目在做，在湛江大学城做外卖和宵夜等，来钱比较快。后续还有一系列的规划，很厉害。学习方面也比较积极。","无","2021/10/15谈话内容：近期学习情况、性格、就业意向、擅长技术，以及短期规划。")'
    """
    # insert_sql = 'insert ignore into students values(2019040434,"林文旭","大数据采集4班","山高组","开朗，有上进心，有想法并能付诸实践。","想从事本专业相关工作，但具体哪个方向还没考虑好。","底子好，也很认真的学习，报过几个课程或考试，如web前端、国家计算机2级、网络工程师、数据库工程师。并于近期会参加前端考试。并且之前暑假的时候就想找过这方面实习。","web、mysql","2021-09-18谈话内容：性格、就业意向、擅长技术、以及对自己未来的规划。")'
    data = '2019040419,"林文旭","大数据采集4班","山高组","开朗，有上进心，有想法并能付诸实践。","想从事本专业相关工作，但具体哪个方向还没考虑好。","底子好，也很认真的学习，报过几个课程或考试，如web前端、国家计算机2级、网络工程师、数据库工程师。并于近期会参加前端考试。并且之前暑假的时候就想找过这方面实习。","web、mysql","2021-09-18谈话内容：性格、就业意向、擅长技术、以及对自己未来的规划。"'
    insert_sql = f'insert ignore into {table_name} values ({data})'
    try:
        cursor.execute(insert_sql)
        connection.commit()
        print(f"数据插入成功！{insert_sql}")
    except:
        traceback.print_exc()
        return -1


def query_table():
    """查询数据"""
    query_sql = f"select * from {table_name}"
    cursor.execute(query_sql)
    result = cursor.fetchall()  #  获取所有数据
    result = cursor.fetchone()  # 获取一条数据
    result = cursor.fetchmany(5)  # 获取5跳数据
    print(result)
    print(len(result))


def run():
    if create_table() == -1:
        print("表格创建失败，程序即将退出！")
        exit()

    insert_table()  #  错误处理
    query_table()


if __name__ == '__main__':
    run()
