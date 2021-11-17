import time
from selenium import webdriver

webdriver_path = r'/Users/muyun/Desktop/pythonProject/jingMaoEducation/chromedriver 2'

"""
1. driver对象的常用属性和方法: 在使用selenium过程中，实例化driver对象后，driver对象有一些常用的属性和方法
    1) driver.page_source 当前标签页浏览器渲染之后的网页源代码
    2) driver.current_url 当前标签页的url
    3) driver.close() 关闭当前标签页，如果只有一个标签页则关闭整个浏览器
    4) driver.quit() 关闭浏览器
    5) driver.forward() 页面前进
    6) driver.back() 页面后退
    7) driver.screen_shot(img_name) 页面截图
"""
"""
2. driver对象定位标签元素获取标签对象的方法: 在selenium中可以通过多种方式来定位标签，返回标签元素对象
    find_element_by_id (返回一个元素) 
    find_element(s)_by_class_name (根据类名获取元素列表) 
    find_element(s)_by_name (根据标签的name属性值返回包含标签对象元素的列表) 
    find_element(s)_by_xpath (返回一个包含元素的列表) 
    find_element(s)_by_link_text (根据连接文本获取元素列表) 
    find_element(s)_by_partial_link_text (根据链接包含的文本获取元素列表) 
    find_element(s)_by_tag_name (根据标签名获取元素列表) 
    find_element(s)_by_css_selector (根据css选择器来获取元素列表)
"""


def demo1():
    """基础用法"""
    driver = webdriver.Chrome(webdriver_path)
    driver.get('https://www.baidu.com')
    # 等待
    time.sleep(3)
    # 通过xpath好到输入框，并输入python
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
    # 通过xpath查找元素，点击
    driver.find_element_by_xpath('//*[@id="su"]').click()
    # 通过id查找元素，点击
    driver.find_element_by_id("su").click()
    # 截图
    driver.save_screenshot("71_screenshot.png")

    print(driver.page_source)  # 源码
    print(driver.current_url)  # 目前的url
    print(driver.back())  # 返回

    time.sleep(6)
    driver.quit()  # 退出


def demo2():
    """selenium标签页的切换"""
    driver = webdriver.Chrome(webdriver_path)
    driver.get("https://www.baidu.com/")
    time.sleep(1)
    driver.find_element_by_id('kw').send_keys('python')
    time.sleep(1)
    driver.find_element_by_id('su').click()
    time.sleep(1)

    # 通过执行js来新开一个标签页
    js = 'window.open("https://www.sogou.com");'
    driver.execute_script(js)
    time.sleep(1)

    # 显示当前所有窗口
    windows = driver.window_handles
    print(windows)
    time.sleep(2)

    # 根据窗口索引进行切换
    # 之前版本的"driver.switch_to_window()" 改成了 "driver.switch_to.window()"
    driver.switch_to.window(windows[0])  # 切换到第一个窗口
    time.sleep(4)
    driver.switch_to.window(windows[1])  # 切换到第二个窗口
    time.sleep(3)
    driver.quit()  # 退出


def demo3():
    """
    switch_to切换frame标签
    iframe是html中常用的一种技术，即一个页面中嵌套了另一个网页，selenium默认是访问不了
    frame中的内容的，对应的解决思路是 driver.switch_to.frame(frame_element) 。接
    下来我们通过qq空间模拟登陆来学习这个知识点
    """
    driver = webdriver.Chrome(webdriver_path)
    url = "https://i.qq.com/"
    driver.get(url)
    time.sleep(3)

    # 方案一：根据iframe框架的id切换iframe标签
    # driver.switch_to.frame('login_frame')

    # 方案二： 根据iframe框架的xpath路径切换iframe标签
    tag_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
    driver.switch_to.frame(tag_frame)

    # 使用账号密码登陆
    driver.find_element_by_id("switcher_plogin").click()
    time.sleep(1)
    driver.find_element_by_id("u").send_keys("1219258598")
    time.sleep(1)
    driver.find_element_by_id("p").send_keys("111")
    time.sleep(1)
    driver.find_element_by_id("login_button").click()
    time.sleep(3)

    print(driver.title)
    driver.quit()


def demo4():
    """
    cookie处理
    selenium能够帮助我们处理页面中的cookie，比如获取、删除等
    1。 获取cookie：driver.get_cookies()
    2。 删除cookie：driver.delete_cookie()
    cookie中各键等含义：
        name        cookie的名称
        value       cookie对应的值，动态生成的
        domain      服务器域名
        expiry      Cookie有效终止日期
        path        Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie
        httpOnly    防脚本攻击
        secure      在Cookie中标记该变量，表明浏览器和服务器之间的通信协议为加密认证协议。
    """
    driver = webdriver.Chrome(webdriver_path)
    url = "http://www.baidu.com"
    driver.get(url)
    time.sleep(3)

    # 获取cookie
    print(driver.get_cookies())
    # 将cookie转为字典格式
    cookie_dict_list = driver.get_cookies()
    cookie_dict = cookie_dict_list[0] if cookie_dict_list else {}
    print(cookie_dict)

    # 删除一条cookie
    driver.delete_cookie("cookie_name")
    print("cookie1:", driver.get_cookies())  # 再获取cookie看下结果

    # 删除所有cookie
    driver.delete_all_cookies()
    print("cookie2:", driver.get_cookies())

    # 添加cookie
    cookie = {"name": "SERVERID", "value": "bb9e97bd82796bb693d27ffe2ee0c2f5|1636969139|1636969003", }
    driver.get("https://www.ketangpai.com/User/login.html")
    driver.add_cookie(cookie_dict=cookie)
    driver.get("https://www.ketangpai.com/Main/index.html")
    print(driver.get_cookies())
    driver.quit()


def demo5():
    """selenium控制浏览器执行js代码"""
    driver = webdriver.Chrome(webdriver_path)
    driver.get("http://www.qq.com/")
    time.sleep(2)
    """
    window.scrollTo(xpos, ypos)
    xpos: 要在窗口文档显示区左上角显示文档等x坐标
    ypos: 要在窗口文档显示区左上角显示文档等y坐标
    document.body.scrollHeight: body元素的高度，基本上就是页面的高度
    """
    js = 'window.scrollTo(0,500)'  # js语句:向下滚动页面，滚动距离500
    js = 'window.scrollTo(0,document.body.scrollHeight)'  # js语句:向下滚动页面，滚动到最下面
    driver.execute_script(js)  # 执行js语句
    time.sleep(5)
    driver.quit()


def demo6():
    """
    页面等待分类：
        - 强制等待： time.sleep()
        - 隐式等待：掌握
            1.隐式等待针对的是元素定位，隐式等待设置了一个时间，在一段时间内判断元素是否定位成功，如果完成了，就进行下一步.
            2.在设置的时间内没有定位成功，则会报超时加载
        - 显式等待：了解
            1.每经过多少秒就查看一次等待条件是否达成，如果达成就停止等待，继续执行后续代码
            2.如果没有达成就继续等待直到超过规定的时间后，报超时异常
            3.显示等待和隐士等待同时存在时，看谁的时间长，就取谁的等待时间
        - 手动等待：掌握
            1。如果遇到这种场景：页面需要滑动才能触发ajax异步加载，就需要手动等待
            原理：
                - 利用强制等待和隐式等待的思路
                - 不停判断，或"有次数的判断"某一个标签对象是否加载完毕（是否存在）
    """
    # ----------- 隐式等待举例 -----------
    # driver = webdriver.Chrome(webdriver_path)
    # driver.implicitly_wait(10)  # 设置最长等待时间，如果超出时间则报错
    # driver.get("http://www.baidu.com")
    # driver.close()

    # ----------- 显式等待举例 -----------
    # from selenium.webdriver.support.wait import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    # from selenium.webdriver.common.by import By
    # driver = webdriver.Chrome(webdriver_path)
    #
    # driver.get("http://www.baidu.com/")
    #
    # # 显示等待
    # # driver：驱动
    # # timeout：设置超时时间,超过10秒就报错
    # # poll_frequency：查看间隔时间，每隔0.5s就通过链接文本内容定位标签是否存在。如果存在就继续向下执行，不存在如果超过10s就抛出异常
    # WebDriverWait(driver, 10).until(EC.title_is("百度一下，你就知道"))  # EC.title_is()返回bool值
    # WebDriverWait(driver, 10).until(EC.title_contains("百度一下"))  # EC.title_contains()返回bool值
    # driver.quit()

    # ----------- 手动等待 （次案例不能用）-----------
    driver = webdriver.Chrome(webdriver_path)
    url = "https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fbuyertrade.taobao.com%2Ftrade%2Fitemlist%2Flist_bought_items.htm%3Fspm%3Da21bo.jianhua.1997525045.2.6d6911d907TXN5"
    driver.get(url)
    time.sleep(2)

    # 最多判断10次
    for i in range(10):
        try:
            time.sleep(3)
            driver.find_element()
            element = driver.find_element_by_xpath('//div[@class="shop- inner"]/h3[1]/a')
            print(element.get_attribute("href"))
            break
        except:
            js = f'window.scrollTo(0,{i * 500})'
            driver.execute_script(js)

    driver.quit()


def demo7():
    """
    无界面模式
    绝大多数服务器是没有界面的，selenium控制谷歌浏览器也支持无界面模式（又称无头模式）
    """
    # 创建一个配置对象
    options = webdriver.ChromeOptions()
    # 开启无界面模式
    options.add_argument("--headless")
    # 禁用gpu
    options.add_argument("--disable-gpu")

    # 创建一个带有配置的driver对象
    driver = webdriver.Chrome(webdriver_path, chrome_options=options)
    driver.implicitly_wait(5)
    driver.get("http://www.baidu.com")
    driver.save_screenshot("71_screenshot.png")
    print(driver.title)
    driver.quit()


def demo8():
    """selenium使用代理ip"""
    # 创建一个配置对象
    options = webdriver.ChromeOptions()
    # 使用代理
    options.add_argument('--proxy-server=http://xxx.xx.xx.xx:xxxx')

    # 创建带有配置的driver对象
    driver = webdriver.Chrome(webdriver_path, chrome_options=options)
    driver.get("http://www.qq.com")
    print(driver.title)
    driver.quit()



def demo9():
    """
    selenium替换user-agent
    selenium控制谷歌浏览器时，User-Agent默认是谷歌浏览器的
    """
    # 创建配置对象
    options = webdriver.ChromeOptions()

    # 替换ua
    options.add_argument("--user-agent=Mozilla/5.0 HAHA")

    # 创建带有配置的driver对象
    driver = webdriver.Chrome(webdriver_path, chrome_options=options)
    driver.get("http://www.baidu.com")
    print(driver.title)
    driver.quit()


if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    # demo8()
    demo9()
