import scrapy
import json
from zhihu_info_3.items import ZhihuInfo3Item
from redis import Redis

class Zhihu3Spider(scrapy.Spider):
    name = 'zhihu3'
    #allowed_domains = ['www.c.com']
    start_urls = ['https://www.zhihu.com/billboard']
    conn = Redis(host='192.168.1.100',port=6379)

    def parse(self, response):
        
        script_text = response.xpath('//*[@id="js-initialData"]/text()').extract_first()
        dic_text = json.loads(script_text)['initialState']['topstory']['hotList']
        
        zhihu_ranking = 0
        for dic in dic_text:
            zhihu_ranking = zhihu_ranking + 1
            zhihu_url = dic['target']['link']['url']
            zhihu_title = dic['target']['titleArea']['text']
        
            item = ZhihuInfo3Item()
            item['zhihu_url'] = zhihu_url
            item['zhihu_title'] = zhihu_title
            item['zhihu_ranking'] = str(zhihu_ranking)

            ex = self.conn.sadd('zhihu',zhihu_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',zhihu_url)
                yield item
            else:
                print('地址已经存在',zhihu_url)
                yield item
        
