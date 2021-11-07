# 抓取图片视频
# 糗事百科

import requests

if __name__ == '__main__':
    # 抓取图片
    img_url = "https://pic.qiushibaike.com/system/pictures/12466/124664751/medium/WZYTW7RQJZOMMVA3.jpg"
    img_text = requests.get(img_url).content  # content是二进制
    with open("./56_血汗豆.jpg", "wb") as f:
        f.write(img_text)

    # 抓取视频
    video_url = "https://qiubai-video-web.qiushibaike.com/NIN2NWWQEV9LU6KY_hd.mp4"
    response = requests.get(video_url)
    with open("56_带娃.mp4", "wb") as f:
        f.write(response.content)
    print(requests)
