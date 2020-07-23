# 基于Scrapy的B站爬虫

基于Scrapy的B站爬虫的小Demo，可以爬取视频列表的信息，需要安装Redis和MongoDB。
Windows系统下Redis可以用Memurai代替。

## 现有的功能

可以爬取B站视频列表中每个视频的信息：


获取的视频的信息如下：



## 运行爬虫

运行前确保Redis和MongoDB的服务已经开启了。

执行以下命令运行爬虫：

    scrapy crawl BilibiliSpider

默认爬取美食区的视频列表，要换成其他区，需要提供参数：

    scrapy crawl BilibiliSpider -a rid=17

其中`rid`是区ID。
