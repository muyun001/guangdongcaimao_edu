""""""
"""
常用三种数据解析方式：
1、正则表达式解析
2、bs4解析
3、xpath解析
三种解析方式可以混合使用，完全是以结果为导向，只要能拿到想要的数据，是用什么方式不重要。
当完全掌握这些解析方法之后，再考虑性能问题。
"""

# 糗事百科图片解析
import re
import os
import time
import requests


def parse_urls(html):
    """
    使用正则表达式对源码进行解析，拿到图片的url链接
    """
    img_urls = re.findall("<div class=\"thumb\">.*?<img src=\"(.*?)\" alt=.*?<img src", html, re.S)
    img_urls = ["https:" + imgurl for imgurl in img_urls]
    return img_urls


def crawl_imgs(img_urls):
    """通过图片的url抓取图片"""
    path = "./57_糗事百科"
    create_dir(path)

    for index, url in enumerate(img_urls):
        img_text = requests.get(url).content
        with open("{}/{}糗事百科.jpg".format(path, index), "wb") as f:
            f.write(img_text)
        print("写入成功！", index)
        time.sleep(0.5)


def create_dir(path):
    """
    创建文件夹
    """
    if not os.path.exists(path):
        os.mkdir(path)


def main():
    # url = "https://www.qiushibaike.com/imgrank/"
    url = "https://www.qiushibaike.com/imgrank/page/1/"  # 可以更换页数
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("访问出错，状态码为{},即将退出程序".format(response.status_code))
    html = response.text
    with open("57_糗事百科.html", "w", encoding="utf-8") as f:
        f.write(html)
    # with open("57_糗事百科.html", "w", encoding="utf-8") as f:
    #     f.write(html)

    # img_urls = parse_urls(html)
    # crawl_imgs(img_urls)


if __name__ == '__main__':
    main()

    # html = """
    #     <div class="thumb">
    #
    # <a href="/article/124737100" target="_blank">
    # <img src="//pic.qiushibaike.com/system/pictures/12473/124737100/medium/I3Z2X1QR0Z658XVD.jpg" alt="糗事#124737100" class="illustration" width="100%" height="auto">
    # <img src="//pic.qiushibaike.com/system/pictures/12473/124737100/medium/I3Z2X1QR0Z658XVD.jpg" alt="糗事#124737100" class="illustration" width="100%" height="auto"></a>
    # </div>
    #     """
    #
    # # 开始解析图片链接
    # url = re.findall("<div class=\"thumb\">.*?<img src=\"//(.*?)\" alt=.*?<img src", html, re.S)
    # print

    html = """
    
<!DOCTYPE html
PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit" />
<meta name="applicable-device" content="pc">





<title>投稿：[doge][doge][doge] - 糗事百科</title>

<meta name="description" content="投稿：[doge][doge][doge]" />

<meta name="keywords" content="投稿," />
<meta http-equiv="mobile-agent" content="format=html5;url=//www.qiushibaike.com/article/124737100">
<meta http-equiv="mobile-agent" content="format=xhtml;url=//www.qiushibaike.com/article/124737100">
<link rel="canonical" href="//www.qiushibaike.com/article/124737100"/>

<meta name="robots" content="noarchive">
<link href="//static.qiushibaike.com/css/dist/web/v4/app.min.css?v=47ca8654c32eddd67f5c7956e7a49c96" media="screen, projection" rel="stylesheet"
type="text/css" />
<script type='text/javascript'>
// Baidu Automatic push content
var _hmt = _hmt || [];
(function () {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
// gio统计
!function (e, t, n, g, i) { e[i] = e[i] || function () { (e[i].q = e[i].q || []).push(arguments) }, n = t.createElement("script"), tag = t.getElementsByTagName("script")[0], n.async = 1, n.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + g, tag.parentNode.insertBefore(n, tag) }(window, document, "script", "assets.growingio.com/2.1/gio.js", "gio");
gio('init', 'ff2672c245bd193c6261e9ab2cd35865', {});
gio('send');
// 收集运营上缓存证据
window.config = {
'user_time': '2021-10-01 19:34:20',
'version': '2017-09-04 14:36'
}
</script>
</head>
<body>


<!-- 单贴页头部 -->
<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/">
<h1>糗事百科</h1>
</a>
</div>
<div id="menu" class="menu-bar menu clearfix">
<a href="/" target="_blank" rel="nofollow">推荐</a>
<a href="/video/" target="_blank">视频</a>
<!-- <a href="/hot/" target="_blank">24小时</a> -->
<a href="/imgrank/" target="_blank">热图</a>
<a href="/text/" target="_blank">段子</a>
<!-- <a href="/history/" target="_blank">穿越</a> -->
<!-- <a href="/pic/" target="_blank">糗图</a> -->
<!-- <a href="/textnew/" target="_blank">新鲜</a> -->
</div>
<div class="download">
下载糗百APP
<div class="download-code">
<img src="//static.qiushibaike.com/images/web/v4/code.png?v=ff5fd05544f168c8059f7a9d84b70302" alt="扫码下载糗百APP" />
<p>扫码下载糗百APP</p>
</div>
</div>
</div>
</div>


<div id="content" class="main">
<div class="content-block clearfix">

<!-- 左边sidebar -->
<div class="col0">
<div class="detail-col0" id="articleSideLeft">
<!-- userinfo -->
<div class="side-left-userinfo">

<img src="//pic.qiushibaike.com/system/avtnew/3210/32109037/thumb/20180815155112.jpg" alt="伊豆Tamia" />

<div class="side-user-top">
<a target="_blank" href="/users/32109037/" title="伊豆Tamia"><span class="side-user-name">伊豆Tam...</span></a>

</div>
<div class="side-user-info clearfix">
<div class="side-detail">
<div class="side-line1">3w</div>
<div class="side-line2">好笑</div>
</div>
<div class="side-detail">
<div class="side-line1">19</div>
<div class="side-line2">粉丝</div>
</div>
<div class="side-detail">
<div class="side-line1">157</div>
<div class="side-line2">糗事</div>
</div>
</div>
</div>

<!-- 
<div class="side-left-hot">
<h3><span class="line"></span> TA的热门糗事 <span class="line"></span></h3>
<ul>



























<li class="item clearfix">
<span class="side-seq">1</span>
<a href="/article/124762895" target="_blank">幼儿舞蹈 舞蹈派对</a>
</li>



























<li class="item clearfix">
<span class="side-seq">2</span>
<a href="/article/124759576" target="_blank">早起的痛<img src="https://static.qiushibaike.com/static/images/emoji/qb_s_54.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_54.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_54.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_54.png" align="absmiddle"></a>
</li>



























<li class="item clearfix">
<span class="side-seq">3</span>
<a href="/article/124745099" target="_blank">刚买的增湿器，大伙看看怎么样？</a>
</li>























<li class="item clearfix">
<span class="">4</span>
<a href="/article/124737100" target="_blank">投稿：<img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"></a>
</li>



























<li class="item clearfix">
<span class="">5</span>
<a href="/article/124731939" target="_blank">韦一敏现象已经开始人传人了吗</a>
</li>

</ul>
</div>
 -->
<!--  -->
<!-- 左边栏ggao1 -->


</div>
</div>




<div class="col1 new-style-col1" data-bj="False">
<!-- ggao1 -->

<h1 class="article-title">

伊豆Tamia的糗事：投稿：<img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"></h1>
<div class="stats">
<span class="stats-time">
2021-09-15 22:22
</span>

<span class="stats-vote">好笑数：<i class="number">287</i></span>

<!-- <div class="source">

<a href="/pic/" class="source-column">发表在：搞笑图片</a>

</div> -->
</div>
<!-- ggao2 -->

<!-- 文章详情页 -->

<div class="article block untagged noline" id='qiushi_tag_124737100'>
<input type="hidden" id="hid">
<div class="image" id="single-next-link" title="下一条">


<div class="content">投稿：<img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"><img src="https://static.qiushibaike.com/static/images/emoji/qb_s_17.png" align="absmiddle"></div>

<div class="thumb">



<img src="//pic.qiushibaike.com/system/pictures/12473/124737100/medium/I3Z2X1QR0Z658XVD.jpg" alt="投稿：<" />
</div>


</div>

<div class='page-nav-list hidden'>
<div id='single-pre-link' class='page-nav-list-bian page-nav-list-pre'>上一条</div>
<div id='single-next-link-button' class='page-nav-list-next'>下一条，你懂的</div>
<div id='single-coll' class='page-nav-list-bian page-nav-list-coll'>收藏本页面</div>
</div>
<!-- 分享 -->
<div id="comments-num qiushi_counts_124737100" class="fs-m mb-m comments-num clearfix">

<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
</div>
</div>












<input type="hidden" value = "124737100" id='articleCurrentLink' />
<input type="hidden" value = "/article/124642556" id='articleNextLink' />
<input type="hidden" value = "/article/124592955" id='articlePreLink' />
<input type="hidden" value =1 id='isArticle' />
<!-- 评论 -->
<div class="cmt-border-top"></div>


<!-- 所以评论-->
<!-- <div class="comments-wrapper" id="all-cmt">
<div id="qiushi_comments_124737100" class="comments">
<div id="r124737100" class="comments-list comments-all clearfix" style="border:none;margin-top:30px">
<div class="comment-title">所有评论</div>
<div class="comment-list clearfix"></div>
<div class="comment-loader">正在加载评论，请稍后...</div>
<div class="pager">
<ul class="comment-pagination pagination clearfix"></ul>
</div>
</div>
</div>
</div> -->
<!-- 相关推荐 -->
<div class="recommend-article">
<h2>相关推荐</h2>
<ul>


<!-- 相关推荐item -->




























<li class="item typs_multi" id='qiushi_tag_124782850'>
<a class="recmd-left multi" href="/article/124782850" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-multi','chick'])">







<img src="//pic.qiushibaike.com/article/image/CFSYYKXMC69P5NQ4.jpg?imageView2/1/w/150/h/112" alt="看我家的狗子像不像堵">

<div class="recmd-tag">2图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124782850" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">看我家的狗子像不像堵在高速上的你</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>163</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/20490109/">

<img src="//pic.qiushibaike.com/system/avtnew/2049/20490109/thumb/20180405080156.JPEG?imageView2/1/w/50/h/50" alt="嗞尿坑人部总裁" />

<span class="recmd-name">嗞尿坑人...</span>
</a>
</div>
</div>
</li>




<!-- 相关第二个广告位item -->
<li class="item" id='qiushi_recom_list_ad'>
<a class="recmd-left" target="_blank" href="https://www.qiushibaike.com/download">
<img src="//static.qiushibaike.com/images/web/v4/textDefault.png?v=12eaf94cfd4d3ae0423a3925bb5bbf9c" />
</a class="recmd-left">
<div class="recmd-right">
<a class="recmd-content" href="https://www.qiushibaike.com/download" target="_blank"></a>
<div class="recmd-detail clearfix">
<a class="recmd-user">
<img src="//static.qiushibaike.com/images/web/v4/logo2.png?v=7d148556f0e5e0ce0ae3b6266802b478" alt="嗞尿坑人部总裁" />
<span class="recmd-name">糗事百科</span>
</a>
</div>
</div>
</li>



<!-- 相关推荐item -->




























<li class="item typs_video" id='qiushi_tag_124767426'>
<a class="recmd-left video" href="/article/124767426" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">





<img src="//qiubai-video-web.qiushibaike.com/EKXMMDMJXT3AJ56O_hd.jpg?imageView2/1/w/150/h/112" alt="到底有多少人对fur">

<div class="recmd-tag">0:29</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124767426" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">到底有多少人对furry控有误解？</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>381</span><span>好笑</span>


<span>·</span>


<span>1</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/33295712/">

<img src="//pic.qiushibaike.com/system/avtnew/3329/33295712/thumb/20180815155106.jpg?imageView2/1/w/50/h/50" alt="开心COCO爱木木" />

<span class="recmd-name">开心CO...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->




























<li class="item typs_video" id='qiushi_tag_124779206'>
<a class="recmd-left video" href="/article/124779206" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">





<img src="//qiubai-video-web.qiushibaike.com/2C373F3D6VA3WZUQ_hd.jpg?imageView2/1/w/150/h/112" alt="妈妈买衣服降价就是带">

<div class="recmd-tag">2:12</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124779206" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">妈妈买衣服降价就是带劲</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>279</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/31418639/">

<img src="//pic.qiushibaike.com/system/avtnew/3141/31418639/thumb/20200922225531.jpg?imageView2/1/w/50/h/50" alt="扎针狂魔小护士" />

<span class="recmd-name">扎针狂魔...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_word" id='qiushi_tag_124445148'>
<a class="recmd-left word" href="/article/124445148" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-word','chick'])">


<img src="//static.qiushibaike.com/images/web/v4/textDefault.png?v=12eaf94cfd4d3ae0423a3925bb5bbf9c" alt="病卧在床上，小儿关切" />

<div class="recmd-tag">纯文</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124445148" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">病卧在床上，小儿关切的问：妈妈，你是要去世了吗？我：你知道去世是什么意思？小儿：去世就是死了啊。爷爷就是生病躺着躺着就去世了的。我惊慌的坐了起来小儿：爷爷去世之</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>1773</span><span>好笑</span>


<span>·</span>


<span>42</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/6013946/">

<img src="//pic.qiushibaike.com/system/avtnew/601/6013946/thumb/20210921113501.jpg?imageView2/1/w/50/h/50" alt="十一朵" />

<span class="recmd-name">十一朵</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_image" id='qiushi_tag_124779866'>
<a class="recmd-left image" href="/article/124779866" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-image','chick'])">





<img src="//pic.qiushibaike.com/system/pictures/12477/124779866/small/GFCDSB502B10SWR1.jpg?imageView2/1/w/150/h/112" alt="是真的我家狗子就代替">

<div class="recmd-tag">1图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124779866" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">是真的我家狗子就代替我出去上学然后上班再然后我就成了废了被扫地出门！！！</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>69</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/42660096/">

<img src="//pic.qiushibaike.com/system/avtnew/4266/42660096/thumb/20210913135412.jpg?imageView2/1/w/50/h/50" alt="不说你也应该懂的" />

<span class="recmd-name">不说你也...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->




























<li class="item typs_multi" id='qiushi_tag_124780175'>
<a class="recmd-left multi" href="/article/124780175" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-multi','chick'])">







<img src="//pic.qiushibaike.com/article/image/4PH5LZB5L9R0YRMV.jpg?imageView2/1/w/150/h/112" alt="千万不要随便吃女朋友">

<div class="recmd-tag">2图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124780175" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">千万不要随便吃女朋友的东西，进嘴的是奶片，出来的是一张脸。。。</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>88</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/45490934/">

<img src="//pic.qiushibaike.com/system/avtnew/4549/45490934/thumb/default_avatar.jpg?imageView2/1/w/50/h/50" alt="糗友2RYCDI" />

<span class="recmd-name">糗友2R...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_word" id='qiushi_tag_124780445'>
<a class="recmd-left word" href="/article/124780445" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-word','chick'])">


<img src="//static.qiushibaike.com/images/web/v4/textDefault.png?v=12eaf94cfd4d3ae0423a3925bb5bbf9c" alt="知乎上看到的:我爸一" />

<div class="recmd-tag">纯文</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124780445" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">知乎上看到的:我爸一老同事，十几年前的时候在派出所值班，半夜无聊放录像带看鬼片。正准备看到高潮的时候，有个人在身后拍了他肩膀，他抬头，一个满脸血污的人在盯着他。</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>358</span><span>好笑</span>


<span>·</span>


<span>3</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/8034692/">

<img src="//pic.qiushibaike.com/system/avtnew/803/8034692/thumb/20170507133959.JPEG?imageView2/1/w/50/h/50" alt="好好学习姐" />

<span class="recmd-name">好好学习...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_image" id='qiushi_tag_124777758'>
<a class="recmd-left image" href="/article/124777758" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-image','chick'])">





<img src="//pic.qiushibaike.com/system/pictures/12477/124777758/small/2N2GUOUP8SUR8FJ6.jpg?imageView2/1/w/150/h/112" alt="人是怎么死的，就是被">

<div class="recmd-tag">1图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124777758" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">人是怎么死的，就是被烦死的。</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>257</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/16719979/">

<img src="//pic.qiushibaike.com/system/avtnew/1671/16719979/thumb/20181018214433.jpg?imageView2/1/w/50/h/50" alt="漫画冯火" />

<span class="recmd-name">漫画冯火</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->




























<li class="item typs_video" id='qiushi_tag_124780792'>
<a class="recmd-left video" href="/article/124780792" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">





<img src="//qiubai-video-web.qiushibaike.com/MV2E0DN9DFJRC03C_hd.jpg?imageView2/1/w/150/h/112" alt="一个人的生活好快乐">

<div class="recmd-tag">0:44</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124780792" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">一个人的生活好快乐</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>147</span><span>好笑</span>


<span>·</span>


<span>1</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/37168772/">

<img src="//pic.qiushibaike.com/system/avtnew/3716/37168772/thumb/20210703001653.jpg?imageView2/1/w/50/h/50" alt="名字太俊不提也罢" />

<span class="recmd-name">名字太俊...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_image" id='qiushi_tag_124779684'>
<a class="recmd-left image" href="/article/124779684" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-image','chick'])">





<img src="//pic.qiushibaike.com/system/pictures/12477/124779684/small/MJ00RB7CCFN22KRV.jpg?imageView2/1/w/150/h/112" alt="莎士比鸭（就算是鸭也">

<div class="recmd-tag">1图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124779684" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">莎士比鸭（就算是鸭也要走在时尚最前沿☜）</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>175</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/46605898/">

<img src="//pic.qiushibaike.com/system/avtnew/4660/46605898/thumb/20210929152105.jpg?imageView2/1/w/50/h/50" alt="露丫。" />

<span class="recmd-name">露丫。</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->




























<li class="item typs_video" id='qiushi_tag_124766232'>
<a class="recmd-left video" href="/article/124766232" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">





<img src="//qiubai-video-web.qiushibaike.com/M1U1C370W7X6ZYB1_hd.jpg?imageView2/1/w/150/h/112" alt="21世纪伟大发明！奇">

<div class="recmd-tag">2:30</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124766232" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">21世纪伟大发明！奇葩单品开箱！</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>287</span><span>好笑</span>


<span>·</span>


<span>5</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/40983270/">

<img src="//pic.qiushibaike.com/system/avtnew/4098/40983270/thumb/20190324020011.jpg?imageView2/1/w/50/h/50" alt="龚民" />

<span class="recmd-name">龚民</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_image" id='qiushi_tag_124781581'>
<a class="recmd-left image" href="/article/124781581" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-image','chick'])">





<img src="//pic.qiushibaike.com/system/pictures/12478/124781581/small/3JWP89FWO32WNKSW.jpg?imageView2/1/w/150/h/112" alt="加我也没用，你们的爷">

<div class="recmd-tag">1图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124781581" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">加我也没用，你们的爷爷不是我抓走的</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>217</span><span>好笑</span>


<span>·</span>


<span>16</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/40088065/">

<img src="//pic.qiushibaike.com/system/avtnew/4008/40088065/thumb/20190831061711.jpg?imageView2/1/w/50/h/50" alt="狐小乔" />

<span class="recmd-name">狐小乔</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_word" id='qiushi_tag_124442518'>
<a class="recmd-left word" href="/article/124442518" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-word','chick'])">


<img src="//static.qiushibaike.com/images/web/v4/textDefault.png?v=12eaf94cfd4d3ae0423a3925bb5bbf9c" alt="伙计们，怎么办，我1" />

<div class="recmd-tag">纯文</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124442518" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">伙计们，怎么办，我15岁的儿子也常常会偷穿我的文胸，我又不好直接批评教育他，毕竟是我这个做父亲的太忙了，忽略了他感受！</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>998</span><span>好笑</span>


<span>·</span>


<span>29</span><span>评论</span>

</div>
<a class="recmd-user" href="/users/43941957/">

<img src="//pic.qiushibaike.com/system/avtnew/4394/43941957/thumb/default_avatar.jpg?imageView2/1/w/50/h/50" alt="糗友quM6Qo" />

<span class="recmd-name">糗友qu...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_image" id='qiushi_tag_124778536'>
<a class="recmd-left image" href="/article/124778536" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-image','chick'])">





<img src="//pic.qiushibaike.com/system/pictures/12477/124778536/small/M4SLLDGM5CKM51MQ.jpg?imageView2/1/w/150/h/112" alt="听说身上有痣的人是你">

<div class="recmd-tag">1图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124778536" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">听说身上有痣的人是你上辈子被人亲吻的地方。</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>172</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/29074014/">

<img src="//pic.qiushibaike.com/system/avtnew/2907/29074014/thumb/2016121111185069.JPEG?imageView2/1/w/50/h/50" alt="撒旦的烈火" />

<span class="recmd-name">撒旦的烈...</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->




























<li class="item typs_multi" id='qiushi_tag_124782894'>
<a class="recmd-left multi" href="/article/124782894" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-multi','chick'])">







<img src="//pic.qiushibaike.com/article/image/5VL3I31Z7RQZLCOF.jpg?imageView2/1/w/150/h/112" alt="今日笑哈哈图1：原来">

<div class="recmd-tag">4图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124782894" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">今日笑哈哈图1：原来篮球场也可以拍证件照图2：如何做到在军训中万众瞩目图3：某位清华大学的同学，你捐的衣服非洲兄弟收到了图4：小心碰头的提示不起作用</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>111</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/45469596/">

<img src="//pic.qiushibaike.com/system/avtnew/4546/45469596/thumb/20210131152049.jpg?imageView2/1/w/50/h/50" alt="有趣大锅" />

<span class="recmd-name">有趣大锅</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->




























<li class="item typs_multi" id='qiushi_tag_124780199'>
<a class="recmd-left multi" href="/article/124780199" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-multi','chick'])">







<img src="//pic.qiushibaike.com/article/image/SVNBWYC5U74LP5DL.jpg?imageView2/1/w/150/h/112" alt="一个瓦匠，带一个腻子">

<div class="recmd-tag">2图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124780199" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">一个瓦匠，带一个腻子铲，很合理吧</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>114</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/36495984/">

<img src="//pic.qiushibaike.com/system/avtnew/3649/36495984/thumb/20200616110150.jpg?imageView2/1/w/50/h/50" alt="阳頂天" />

<span class="recmd-name">阳頂天</span>
</a>
</div>
</div>
</li>




<!-- 相关推荐item -->
























<li class="item typs_image" id='qiushi_tag_124781973'>
<a class="recmd-left image" href="/article/124781973" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-image','chick'])">





<img src="//pic.qiushibaike.com/system/pictures/12478/124781973/small/522YULWW2QKZICVQ.jpg?imageView2/1/w/150/h/112" alt="这…………">

<div class="recmd-tag">1图</div>
</a>
<div class="recmd-right">
<a class="recmd-content" href="/article/124781973" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">这…………</a>
<div class="recmd-detail clearfix">
<div class="recmd-num">

<span>164</span><span>好笑</span>



</div>
<a class="recmd-user" href="/users/3233088/">

<img src="//pic.qiushibaike.com/system/avtnew/323/3233088/thumb/20190113191020.jpg?imageView2/1/w/50/h/50" alt="帕特里克H" />

<span class="recmd-name">帕特里克...</span>
</a>
</div>
</div>
</li>



</ul>
</div>


<a target="_blank" href="https://www.qiushibaike.com/download">
<img style="width: 608px;" src="//static.qiushibaike.com/images/web/v4/bottom_banner.png?v=abe550db6041a436de88f4fa95f9f7ed" />
</a>
</div>


<div class="col2">
<div id="sidebar" class="sidebar">





<!-- APP下载引导二维码 -->
<div class="qrcode-wrap">
<img class="qrcode-wrap-img" src="//static.qiushibaike.com/images/web_v3/sidebar/qrcode_banner.png?v=14387788b9eb2f53bc951e7a3bb1f939"
alt="糗事百科 APP 下载二维码">
</div>
</div>
</div>




</div>
</div>


<div class="foot">
<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="https://hr.qiushibaike.com/about.html" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="https://hr.qiushibaike.com/social.html" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="https://hr.qiushibaike.com/about.html?tag=3" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="//about.qiushibaike.com/touch_agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="//about.qiushibaike.com/law/privacy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
推荐
</h3>
<ul>
<li>
<a href="/joke/" target="_blank">
搞笑合集
</a>
</li>
<li>
<a href="/history/" target="_blank">
历史回顾
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<p><a style='color:#333' href="https://beian.miit.gov.cn">互联网ICP备案：京ICP备14028348号-1</a></p>
<p>
<span>广播电视节目制作经营许可证：（京）字第08319号</span>
<span>网络文化经营许可证：
<img src="//static.qiushibaike.com/images/wenhuajingying.png?v=f5f3976cf4be787ad2be202a19d40823"
style='width: 20px; height: 20px; vertical-align: top;'>京网文[2020]0625-100号
</span>
</p>
<p style="margin-top: 8px">增值电信业务经营许可证：京ICP证140448号</p>
<!-- <p style="margin-top: 8px"><span>营业性演出许可证：京演(机构)(2018)1940号</span></p> -->
<p>
<span><a style='color:#333' target="_blank"
href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601"
rel="nofollow"><img style='vertical-align: top;'
src="//static.qiushibaike.com/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a></span>
<span>守护未成年专用邮箱：young@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">
<a style='color:#333' href="https://www.12377.cn/">网上有害信息举报专区</a>
</p>
<p>
<span>违法和不良信息举报电话：18126520579</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">
友际无限（北京）科技有限公司
</p>
<p>
<span>&copy; Qiushibaike.com 糗事百科版权所有</span>
</p>
</div>
</div>


<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="//static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v4/app.min.js?v=fbc16cfe4c15c40a97da39f0a102b992"></script>



<script type="text/javascript">
// Google Analytics
(function (i, s, o, g, r, a, m) {
i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
(i[r].q = i[r].q || []).push(arguments)
}, i[r].l = 1 * new Date(); a = s.createElement(o),
m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>

<script type="text/javascript" async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script type="text/javascript" src="https://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">




window.broadJson = '[]'
</script>
<!-- <script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v3/adsAdmin.min.js?v=9c42f35ae43e17caf141e9d6ebe32cbb"></script> -->
</body>
</html>
    """
