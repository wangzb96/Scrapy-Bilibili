from typing import Generator
import redis


class Container:
    def __len__(self) -> int:
        """返回容器中元素个数"""
        return self.size()
    def __contains__(self, *args, **kwargs) -> bool:
        """判断元素是否存在于容器中"""
        return self.has(*args, **kwargs)
    def __iter__(self) -> Generator:
        """迭代访问容器中的所有元素"""
        return self.iter()

    def size(self) -> int:
        """返回容器中元素个数"""
        pass
    def has(self, *args, **kwargs) -> bool:
        """判断元素是否存在于容器中"""
        pass
    def iter(self) -> Generator:
        """迭代访问容器中的所有元素"""
        pass


class Set(Container):
    def insert(self, *args, **kwargs):
        """插入一个元素"""
        pass
    def delete(self, *args, **kwargs):
        """删除一个元素"""
        pass

    def inserts(self, *args, **kwargs):
        """插入多个元素"""
        pass
    def deletes(self, *args, **kwargs):
        """删除多个元素"""
        pass


class Redis:
    def __init__(self, cp: bool=None, cs: int=None, *args, **kwargs):
        """初始化

            Args:
                cp: 是否使用连接池，默认否
                cs: 连接池的最大连接数，默认8
        """

        kwargs['decode_responses'] = True  # 使Redis默认返回字符串
        if cp:
            if cs is None: cs = 8
            cp = redis.ConnectionPool(max_connections=cs)
            kwargs['connection_pool'] = cp
        self.redis = redis.Redis(*args, **kwargs)

    def getSet(self, key: str):
        """返回集合容器

            Args:
                key: 集合的名字
        """

        return Redis.Set(self.redis, key)

    class Container:
        def __init__(self, redis, key: str):
            self.redis = redis
            self.key = key
            self.pipeline = None

        def getRedis(self):
            if self.pipeline: return self.pipeline
            return self.redis

        def getPipeline(self):
            if self.pipeline: return False
            self.pipeline = self.redis.pipeline()
            return True
        def execute(self):
            if self.pipeline:
                r = self.pipeline.execute()
                self.pipeline = None
                return r

    class Set(Container, Set):
        def __init__(self, redis, key: str):
            super().__init__(redis, key)

        def size(self):
            return self.getRedis().scard(self.key)
        def has(self, x):
            return self.getRedis().sismember(self.key, x)
        def iter(self):
            return self.getRedis().smembers(self.key)

        def insert(self, x):
            return self.inserts(x)
        def delete(self, x):
            return self.deletes(x)

        def inserts(self, x, *args):
            return self.getRedis().sadd(self.key, x, *args)
        def deletes(self, x, *args):
            return self.getRedis().srem(self.key, x, *args)


if __name__=='__main__':
    redis = Redis(cp=True)
    set = redis.getSet('BilibiliVideoList76')
    print([set.size(), list(set.iter())])

    set.inserts('Hello', 'world', 'world!', 'Hello', 'lalala')
    print([set.size(), list(set.iter())])

    set.deletes('lala')
    print([set.size(), list(set.iter())])

    set.deletes('lalala')
    print([set.size(), list(set.iter())])
