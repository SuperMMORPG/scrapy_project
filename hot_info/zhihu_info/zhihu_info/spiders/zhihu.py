import scrapy
from redis import Redis
from time import sleep
from selenium import webdriver
from zhihu_info.items import ZhihuInfoItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://www.zhihu.com/search?type=content&q=1']

    conn = Redis(host='192.168.1.100',port=6379)

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='./chromedriver.exe')

    def parse(self, response):
        div_list = response.xpath('//*[@id="root"]/div/main/div/div[2]/div[3]/div/div/div/div/div[2]/div')
        zhihu_ranking = 0
        for div in div_list:
            zhihu_ranking = zhihu_ranking + 1

            href = div.xpath('./a/@href').extract_first()
            zhihu_url = 'https://www.zhihu.com' + href
            zhihu_title = div.xpath('./a/span/text()').extract_first()
            
            item = ZhihuInfoItem()
            item['zhihu_ranking'] = str(zhihu_ranking)
            item['zhihu_url'] = zhihu_url
            item['zhihu_title'] = zhihu_title

            ex = self.conn.sadd('zhihu',zhihu_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',zhihu_url)
                yield item
            else:
                print('地址已经存在',zhihu_url)
                yield item


    def closed(self,spider):
        sleep(5)
        self.bro.quit()


