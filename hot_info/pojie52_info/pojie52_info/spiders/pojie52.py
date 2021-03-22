import scrapy
from redis import Redis
from pojie52_info.items import Pojie52InfoItem

class Pojie52Spider(scrapy.Spider):
    name = 'pojie52'
    start_urls = ['https://www.52pojie.cn/forum.php']
    conn = Redis(host='192.168.1.100',port=6379)

    def parse(self, response):
        ranking = 0
        # tbody标签去除             //*[@id="category_"]/table/tbody/tr[2]/td[3]/div
        div_list = response.xpath('//*[@id="category_"]/table/tr[2]/td[3]/div/div')

        #text = response.body.decode(response.encoding)
        #with open('./a.html','w',encoding='utf8') as fp:
        #    fp.write(text)
        
        for div in div_list:

            url = 'https://www.52pojie.cn/' + div.xpath('./a/@href').extract_first()
            title = div.xpath('./a/text()').extract_first()
            ranking = ranking + 1

            item = Pojie52InfoItem()
            item['url'] = url
            item['title'] = title
            item['ranking'] = ranking

            ex = self.conn.sadd('52pojie',url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item
        