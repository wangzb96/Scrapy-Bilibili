# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from database import MongoDataBase
from container import Redis


class BilibiliPipeline:
    def __init__(self):
        """初始化"""

        # 数据库对象
        self.dataBase = MongoDataBase()
        # 数据表对象，负责数据保存
        self.datas = self.dataBase.getDatas('bilibili', 'video_list')
        # 缓存对象
        self.redis = Redis(cp=True)
        # 集合对象，负责数据去重
        self.set = self.redis.getSet('bilibili_video_list')

    def process_item(self, item, spider):
        """处理Item对象

            对Item对象用Redis的Set进行去重，然后存入MongoDB。
        """

        bvid = item['bvid']  # 视频ID
        if bvid not in self.set:  # 如果视频ID不在集合中
            self.set.insert(bvid)  # 视频ID加入集合
            self.datas.insert(dict(item))  # Item对象转成字典存入数据库
        return item


if __name__=='__main__':
    pass

