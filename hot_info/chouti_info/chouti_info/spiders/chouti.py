import scrapy
from selenium import webdriver
from time import sleep
from redis import Redis
from chouti_info.items import ChoutiInfoItem

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    #allowed_domains = ['ww.xx.com']
    start_urls = ['https://dig.chouti.com/']
    conn = Redis(host='192.168.1.100',port=6379)

    def __init__(self):

        self.bro = webdriver.Chrome(executable_path='./chromedriver.exe')

    def parse(self, response):
        
        #解析页面，分别得到3个时间的热门参数
        div_list = response.xpath('/html/body/main/div/div/div[2]/div/div[4]/div[2]/div')
        div_24 = div_list[0]
        div_72 = div_list[1]
        div_168 = div_list[2]

        a_24 = div_24.xpath('./a')
        a_72 = div_72.xpath('./a')
        a_168 = div_168.xpath('./a')
        
        ranking_24 = 0
        for a in a_24:

            ranking_24 = ranking_24 + 1
            href = a.xpath('./@href').extract_first()
            url = 'https://dig.chouti.com/' + href
            title = a.xpath('./div[2]/text()').extract_first()

            item = ChoutiInfoItem()
            item['chouti_url'] = url
            item['chouti_title'] = title
            item['chouti_ranking'] = str(ranking_24)
            item['chouti_hours'] = '24'

            ex = self.conn.sadd('chouti',url)
            if ex==1:
                #print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item

        
        ranking_72 = 0
        for a in a_72:
            ranking_72 = ranking_72 + 1
            href = a.xpath('./@href').extract_first()
            url = 'https://dig.chouti.com/' + href
            title = a.xpath('./div[2]/text()').extract_first()

            item = ChoutiInfoItem()
            item['chouti_url'] = url
            item['chouti_title'] = title
            item['chouti_ranking'] = str(ranking_72)
            item['chouti_hours'] = '72'

            ex = self.conn.sadd('chouti',url)
            if ex==1:
                #print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item

        ranking_168 = 0
        for a in a_168:
            ranking_168 = ranking_168 + 1
            href = a.xpath('./@href').extract_first()
            url = 'https://dig.chouti.com/' + href
            title = a.xpath('./div[2]/text()').extract_first()

            item = ChoutiInfoItem()
            item['chouti_url'] = url
            item['chouti_title'] = title
            item['chouti_ranking'] = str(ranking_168)
            item['chouti_hours'] = '168'
            
            ex = self.conn.sadd('chouti',url)
            if ex==1:
                #print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item
        

    def closed(self,spider):
        sleep(5)
        self.bro.quit()







