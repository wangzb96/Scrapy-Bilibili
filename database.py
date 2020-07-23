import pymongo


class DataBase:
    def getDatas(self, *args, **kwargs):
        """返回数据表对象"""
        pass

    class Datas:
        def insert(self, *args, **kwargs):
            """插入一个数据"""
            pass
        def delete(self, *args, **kwargs):
            """删除一个数据"""
            pass
        def update(self, *args, **kwargs):
            """更新一个数据"""
            pass

        def inserts(self, *args, **kwargs):
            """插入多个数据"""
            pass
        def deletes(self, *args, **kwargs):
            """删除多个数据"""
            pass
        def updates(self, *args, **kwargs):
            """更新多个数据"""
            pass

        def find(self, *args, **kwargs):
            """查找数据"""
            pass


class MongoDataBase(DataBase):
    def __init__(self, *args, **kwargs):
        """初始化"""

        self.mongo = pymongo.MongoClient(*args, **kwargs)

    def getDatas(self, db_key: str, datas_key: str):
        """返回数据表对象

            Args:
                db_key: 数据库名字
                datas_key: 数据表名字
        """

        return MongoDataBase.MongoDatas(self.mongo[db_key][datas_key])

    class MongoDatas(DataBase.Datas):
        def __init__(self, datas):
            self.datas = datas

        def insert(self, d):
            return self.datas.insert_one(d)
        def delete(self, c):
            return self.datas.delete_one(c)
        def update(self, c, d):
            return self.datas.update_one(c, d)

        def inserts(self, d):
            return self.datas.insert_many(d)
        def deletes(self, c):
            return self.datas.delete_many(c)
        def updates(self, c, d):
            return self.datas.update_many(c, d)

        def find(self, *args, **kwargs):
            r = self.datas.find(*args, **kwargs)
            for i in r:
                del i['_id']  # 删除_id属性
                yield i


if __name__=='__main__':
    url = 'mongodb://localhost:27017'
    dataBase = MongoDataBase()
    datas = dataBase.getDatas('bilibili', 'video_list')
    print(list(datas.find()))

    datas.inserts([
        {'ctt':'Hello world!'},
        {'a':123, 'b':3.14, 'c':'lalala', 'd':[999, 555, 111]}
    ])
    print(list(datas.find()))

    datas.deletes({})
    print(list(datas.find()))

