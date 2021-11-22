from redis import StrictRedis

"""
redis: 非关系型数据库
"""
r = StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)


def redis_test():
    # 添加数据
    # r.set("name", "zhangsan")  # 一次性插入一条数据

    # r.mset({"name": "张三", "age": 19, "score": 90})  # 一次性插入多条数据
    # name = r.get("name")  # # 一次性获取一条数据
    # print(name)

    # print(r.mget("name", "age", "score"))  # 一次性获取多条数据

    # r.delete("name")  # 删除数据

    # is_exist = r.exists("name")  # 判断数据是否存在，存在返回1，否则返回0
    # print(is_exist)

    json_data = {
        "name": "zhangsan",
        "age": 19,
        "score": 90
    }

    r.set("student_info", f"{json_data}")


if __name__ == '__main__':
    redis_test()
