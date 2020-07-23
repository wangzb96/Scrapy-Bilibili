# Define here the models for your scraped items
#
# See documentation in:
# https://docs.org/en/latest/topics/items.html

from scrapy import Item, Field


class BilibiliVideoListItem(Item):
    # 视频信息
    aid = Field()  # 视频ID
    bvid = Field()  # 视频ID

    tid = Field()  # 区
    pic = Field()  # 封面
    title = Field()  # 标题
    desc = Field()  # 简介
    duration = Field()  # 总时长，所有分P时长总和
    videos = Field()  # 分P数
    pubdate = Field()  # 发布时间

    view = Field()  # 播放数
    danmaku = Field()  # 弹幕数
    reply = Field()  # 评论数
    like = Field()  # 点赞数
    dislike = Field()  # 点踩数
    coin = Field()  # 投币数
    favorite = Field()  # 收藏数
    share = Field()  # 分享数

    cid = Field()  # 标签ID

    # UP主信息
    mid = Field()  # UP主ID

    name = Field()  # 昵称
    face = Field()  # 头像


if __name__=='__main__':
    item = BilibiliVideoListItem()
    print(item)
    print(dict(item))

