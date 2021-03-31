import scrapy
from selenium import webdriver
from time import sleep
from redis import Redis
from pexels_info.items import PexelsInfoItem
from pexels_info.utils import connect,add
class PexelsSpider(scrapy.Spider):
    name = 'pexels'
    start_urls = ['https://www.pexels.com/leaderboard/all-time/']

    conn = connect()

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='./chromedriver.exe')

    def parse(self, response):

        #text = response.body.decode()
        #with open('./a.html','w',encoding='utf-8') as f:
        #    f.write(text)
        #f.close()

        article_list = response.xpath('/html/body/section/div[3]/article')
        for article in article_list:
            ranking = article.xpath('./div[1]/div[1]/span[1]/text()').extract_first()
            name = article.xpath('./div[1]/div[2]/h3/a/text()').extract_first()
            url = 'https://www.pexels.com' + article.xpath('./div[1]/div[2]/h3/a/@href').extract_first()
        
            item = PexelsInfoItem()
            item['ranking'] = ranking
            item['name'] = name
            item['url'] = url

            add(self.conn,'pexels',url)
            yield item


    def closed(self,spider):
        sleep(3)
        self.bro.quit()

