import scrapy
from redis import Redis
from guancha_info.items import GuanchaInfoItem
class GuanchaSpider(scrapy.Spider):
    name = 'guancha'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://www.guancha.cn/gongye%C2%B7keji']
    conn = Redis(host='127.0.0.1',port=6379)

    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li')
        for i in range(10):
            li = li_list[i]
            guancha_title = li.xpath('./div/h4/a/text()').extract_first()
            href = li.xpath('./div/h4/a/@href').extract_first()
            guancha_url = 'https://www.guancha.cn' + href

            item = GuanchaInfoItem()
            item['guancha_url'] = guancha_url
            item['guancha_title'] = guancha_title
            guancha_ranking = i + 1
            item['guancha_ranking'] = str(guancha_ranking)

            ex = self.conn.sadd('guancha',guancha_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',guancha_url)
                yield item
            else:
                print('地址已经存在',guancha_url)
                yield item