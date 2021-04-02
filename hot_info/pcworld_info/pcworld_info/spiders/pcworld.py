import scrapy
from pcworld_info.items import PcworldInfoItem

class PcworldSpider(scrapy.Spider):
    name = 'pcworld'
    start_urls = ['https://www.pcworld.com/category/laptop-computers/']

    # 动态加载页面
    # url = https://www.pcworld.com/ajaxGetMoreCategory?start=75&catId=3015
    
    def parse(self, response):
        div_list = response.xpath('//*[@id="crawlLatestResults"]/div')
        for div in div_list:

            href = div.xpath('./a/@href').extract_first()
            if href:
                url = 'https://www.pcworld.com' + href
                title = div.xpath('./div/p[1]/a/text()').extract_first().strip()
                up_date = div.xpath('./div/p[2]/span/@title').extract_first()

                item = PcworldInfoItem()

                item['url'] = url
                item['title'] = title
                item['up_date'] = up_date

                yield item

