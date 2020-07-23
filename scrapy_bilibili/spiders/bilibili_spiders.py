from scrapy import Spider, Request
from scrapy_bilibili.items import BilibiliVideoListItem
from util import json2obj


class BilibiliSpider(Spider):
    # Spider名字
    name = 'BilibiliSpider'

    # 视频列表链接模版 （三个参数）
    url_fmt = r'https://api.bilibili.com/x/web-interface/newlist?' \
              r'rid={rid}&type=0&ps={ps}&pn={pn}'

    def __init__(self, *args, rid: int=None, ps: int=None, **kwargs):
        """初始化

            Args:
                rid: 区ID，默认76，表示美食区
                ps: 视频列表每页视频数量，默认100
        """

        super().__init__(*args, **kwargs)

        if rid is None: rid = 76
        if ps is None: ps = 100
        self.rid = rid
        self.ps = ps
        # 视频列表链接模版 （一个参数）
        self.url = self.url_fmt.format(rid=rid, ps=ps, pn='{}')
        # 初始链接
        self.start_urls = [self.url.format(1)]

    def parse(self, response):
        """页面解析"""

        url = response.url
        pn = int(url.rsplit('=', 1)[-1])  # 视频列表页码
        page = response.body.decode('UTF-8')  # 响应对象中的json文件
        obj = json2obj(page)  # 转成Python对象
        data = obj['data']
        count = data['page']['count']  # 该区当前视频总数
        archives = data['archives']
        for i in archives:
            aid = i['aid']
            bvid = i['bvid'].strip()

            tid = i['tid']
            pic = i['pic'].strip()
            title = i['title'].strip()
            desc = i['desc'].strip()
            duration = i['duration']
            videos = i['videos']
            pubdate = i['pubdate']

            stat = i['stat']
            view = stat['view']
            danmaku = stat['danmaku']
            reply = stat['reply']
            like = stat['like']
            dislike = stat['dislike']
            coin = stat['coin']
            favorite = stat['favorite']
            share = stat['share']

            cid = i['cid']

            owner = i['owner']
            mid = owner['mid']

            name = owner['name'].strip()
            face = owner['face'].strip()

            # 封装成Item对象
            item = BilibiliVideoListItem(
                aid=aid,
                bvid=bvid,

                tid=tid,
                pic=pic,
                title=title,
                desc=desc,
                duration=duration,
                videos=videos,
                pubdate=pubdate,

                view=view,
                danmaku=danmaku,
                reply=reply,
                like=like,
                dislike=dislike,
                coin=coin,
                favorite=favorite,
                share=share,

                cid=cid,

                mid=mid,

                name=name,
                face=face,
            )
            yield item

        if pn*self.ps<count:  # 如果当前爬取的视频数量少于视频总数
            url = self.url.format(pn+1)  # 下一页的页码
            req = Request(url, callback=self.parse)  # 下一页的请求对象
            yield req


if __name__=='__main__':
    s = '''{"code":0,"message":"0","ttl":1,"data":{"archives":[{"aid":243910595,"videos":1,"tid":76,"tname":"美食圈","copyright":1,"pic":"http://i0.hdslb.com/bfs/archive/0e13801f9670e8dda8cce15f8090dfacf78f0bea.png","title":"最简单的肉末酱茄子做法！不油不腻，老下饭了！","pubdate":1595396780,"ctime":1595396780,"desc":"肉末酱茄子不油不腻老下饭了","state":0,"attribute":16384,"duration":83,"rights":{"bp":0,"elec":0,"download":0,"movie":0,"pay":0,"hd5":0,"no_reprint":0,"autoplay":1,"ugc_pay":0,"is_cooperation":0,"ugc_pay_preview":0,"no_background":0},"owner":{"mid":638628553,"name":"user_76365067632","face":"http://i0.hdslb.com/bfs/face/1e3e260ad5a14d0dafdd0e1a84eb213ddb7bac95.jpg"},"stat":{"aid":243910595,"view":0,"danmaku":0,"reply":0,"favorite":0,"coin":0,"share":0,"now_rank":0,"his_rank":0,"like":0,"dislike":0},"dynamic":"","cid":215272733,"dimension":{"width":720,"height":1280,"rotate":0},"bvid":"BV1Nv411q78E"}],"page":{"count":1821990,"num":1,"size":1}}}'''
    obj = json2obj(s)
    data = obj['data']
    count = data['page']['count']
    archives = data['archives']
    for i in archives:
        aid = i['aid']
        bvid = i['bvid'].strip()

        tid = i['tid']
        pic = i['pic'].strip()
        title = i['title'].strip()
        desc = i['desc'].strip()
        duration = i['duration']
        videos = i['videos']
        pubdate = i['pubdate']

        stat = i['stat']
        view = stat['view']
        danmaku = stat['danmaku']
        reply = stat['reply']
        like = stat['like']
        dislike = stat['dislike']
        coin = stat['coin']
        favorite = stat['favorite']
        share = stat['share']

        cid = i['cid']

        owner = i['owner']
        mid = owner['mid']

        name = owner['name'].strip()
        face = owner['face'].strip()

        item = BilibiliVideoListItem(
            aid=aid,
            bvid=bvid,

            tid=tid,
            pic=pic,
            title=title,
            desc=desc,
            duration=duration,
            videos=videos,
            pubdate=pubdate,

            view=view,
            danmaku=danmaku,
            reply=reply,
            like=like,
            dislike=dislike,
            coin=coin,
            favorite=favorite,
            share=share,

            cid=cid,

            mid=mid,

            name=name,
            face=face,
        )
        print(item)

