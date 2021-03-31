import scrapy

from rottentomatoes_info.items import RottentomatoesInfoItem
class RottentomatoesSpider(scrapy.Spider):
    name = 'rottentomatoes'
    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/']

    def parse(self, response):

        tr_list = response.xpath('//*[@id="top_movies_main"]/div/table/tr')
        
        for tr in tr_list:
            ranking = tr.xpath('./td[1]/text()').extract_first()
            rating = tr.xpath('./td[2]/span/span[2]/text()').extract_first().strip()
            name = tr.xpath('./td[3]/a/text()').extract_first().strip()
            url = 'https://www.rottentomatoes.com' + tr.xpath('./td[3]/a/@href').extract_first()

            item = RottentomatoesInfoItem()
            item['ranking'] = ranking
            item['rating'] = rating
            item['name'] = name
            item['url'] = url
            yield scrapy.Request(url,callback=self.detail_parse,meta={'item':item})
    
    def detail_parse(self,response):
        
        item = response.meta['item']

        audiencescore = response.xpath('//*[@id="topSection"]/score-board/@audiencescore').extract_first()
        tomatometerscore = response.xpath('//*[@id="topSection"]/score-board/@tomatometerscore').extract_first()

        item['audiencescore'] = audiencescore
        item['tomatometerscore'] = tomatometerscore
        yield item
