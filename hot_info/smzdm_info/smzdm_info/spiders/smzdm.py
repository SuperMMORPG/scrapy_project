import scrapy
from smzdm_info.items import SmzdmInfoItem
from redis import Redis
class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://post.smzdm.com/hot_1/']

    conn = Redis(host='127.0.0.1',port=6379)

    def parse(self, response):
        
        li_list = response.xpath('//*[@id="feed-main-list"]/li')
        for i in range(12):
            li = li_list[i]
            smzdm_url = li.xpath('./div/div[2]/h5/a/@href').extract_first()
            smzdm_title = li.xpath('./div/div[2]/h5/a/text()').extract_first()
            smzdm_ranking = i + 1

            item = SmzdmInfoItem()
            item['smzdm_url'] = smzdm_url 
            item['smzdm_title'] = smzdm_title
            item['smzdm_ranking'] = str(smzdm_ranking)

            ex = self.conn.sadd('smzdm',smzdm_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',smzdm_url)
                yield item
            else:
                print('地址已经存在',smzdm_url)
                yield item



            

