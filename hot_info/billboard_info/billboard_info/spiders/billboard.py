import scrapy
from billboard_info.items import BillboardInfoItem

class BillboardSpider(scrapy.Spider):
    name = 'billboard'

    start_urls = ['https://www.billboard.com/charts/hot-100']

    def parse(self, response):
        
        # 这条信息可以拿到 video 需要做字符串处理
        #text = response.xpath('//*[@id="charts"]/@data-chart-videos').extract()
        
        # 奇怪 路径需要跳过直接到  //ol/li
        li_list = response.xpath('//*[@id="charts"]/div/div[7]//ol/li')
        #print(li_list)
        for li in li_list:
            ranking = li.xpath('./button/span[1]/span[1]/text()').extract_first()
            name = li.xpath('./button/span[2]/span[1]/text()').extract_first()
            author = li.xpath('./button/span[2]/span[2]/text()').extract_first()
        
            item = BillboardInfoItem()
            item['ranking'] = ranking
            item['name'] = name
            item['author'] = author
            yield item
