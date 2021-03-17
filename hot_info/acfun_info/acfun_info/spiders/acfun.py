import scrapy
from selenium import webdriver
from time import sleep
from redis import Redis
from acfun_info.items import AcfunInfoItem

class AcfunSpider(scrapy.Spider):
    name = 'acfun'
    
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://www.acfun.cn/rank/list#cid=-1;range=1']

    conn = Redis(host='192.168.1.100',port=6379)

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='./chromedriver.exe')

    def parse(self, response):
        
        div_list = response.xpath('//*[@id="block"]/div[2]/div')

        for i in range(10):

            item = AcfunInfoItem()

            div = div_list[i]
            title = div.xpath('./div[1]/div[2]/a/text()').extract_first()
            href = div.xpath('./div[1]/div[2]/a/@href').extract_first()
            url = 'https://www.acfun.cn' + href
            rank = str(i + 1)

            item['url'] = url
            item['title'] = title
            item['rank'] = rank

            ex = self.conn.sadd('acfun',url)
            if ex==1:
                #print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item


    def closed(self,spider):
        sleep(3)
        self.bro.quit()
