"""
redis数据库：非关系型数据库
"""

from redis import StrictRedis

r = StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)


def redis_test():
    # 单条数据
    r.set("age", 19)  # 添加数据
    age = r.get("age")  # 获取数据
    print(age)

    # 多条数据
    r.mset({"name": "zhangsan", "age": 19})
    print(r.mget("name", "age"))

    # job_info = {
    #     "job_id": "0006dfe42a764216921b402d401f404f31aee685",
    #     "job_title": "日结丨文字聊天员丨陪伴赚钱",
    #     "job_url": "http://xinyu.jianzhimao.com/job/V3hNODAzUDl4MEE9.html",
    #     "visited": 813,
    # }
    # r.set("0006dfe42a764216921b402d401f404f31aee685",f"{job_info}")
    # print(r.get("0006dfe42a764216921b402d401f404f31aee685"))

    # 删除数据
    r.delete("0006dfe42a764216921b402d401f404f31aee685")


    # 判断是否存在
    score = r.exists("score")  # 如果有就返回1，否则返回0
    print(score)

    if r.exists("score"):
        print(r.get("score"))


if __name__ == '__main__':
    redis_test()
