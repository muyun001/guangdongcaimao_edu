import aiohttp
import asyncio
import aiofiles
import time
import requests
from lxml import etree


async def parse_img_urls(html):
    """解析图片的url"""
    tree = etree.HTML(html)
    srcs = tree.xpath('//ul[@class="ali"]//img/@src')
    srcs = ["https:" + src for src in srcs]
    return srcs


async def crawl_img_urls(page_url):
    """抓取每一页的图片"""
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with session.get(page_url) as resp:
            text = await resp.text()
            urls = await parse_img_urls(text)
            return urls


async def crawl_save_img(img_url):
    """根据图片链接抓取图片，并保存到文件夹中"""
    img_name = img_url.split("/")[-1]
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as s:
        async with s.get(img_url) as r:
            img_content = await r.content.read()
            async with aiofiles.open(f"./79_协程抓取图片1/{img_name}", "wb") as f:
                await f.write(img_content)
                print(img_url)


async def run():
    img_nums = 0
    for i in range(1, 200 + 1):
        page_url = f"https://www.ivsky.com/tupian/index_{i}.html"
        img_urls = await crawl_img_urls(page_url)
        img_nums += len(img_urls)
        print(f"img_nums:{img_nums}")
        if not img_urls:
            print(f"解析到到img_urls为空！page_url:{page_url}")
            continue
        tasks = [asyncio.create_task(crawl_save_img(url)) for url in img_urls]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    print("程序开始")

    start_time = time.time()
    asyncio.run(run())
    end_time = time.time()

    print(f"图片抓取完成，耗时：{end_time - start_time}秒")
