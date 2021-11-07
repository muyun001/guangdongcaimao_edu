# 吉祥数字 100 ~ 999     111 222 333 444 555....   123 234 345 456 567....789    987 876 765 ....321 210
i = 100
while i < 1000:
    # 获取三位一样的数字 111 222 333
    if i % 111 == 0:
        print(i)

    # 获取连续递增的数字
    # 1 将数字转为字符串
    s = str(i)  # 123 ---> "123"
    # 2 拆分字符串s
    bai = s[0]  # "1"
    shi = s[1]  # "2"
    ge = s[2]

    if int(bai) + 1 == int(shi) and int(shi) + 1 == int(ge):
        print(i)

    if int(bai) - 1 == int(shi) and int(shi) - 1 == int(ge):
        print(i)
    i += 1
