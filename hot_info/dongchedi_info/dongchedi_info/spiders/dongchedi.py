import scrapy
from dongchedi_info.items import DongchediInfoItem,DongchediVideoItem,DongchediArticleItem
from redis import Redis
class DongchediSpider(scrapy.Spider):
    name = 'dongchedi'
    start_urls = ['https://www.dongchedi.com/feed']

    conn = Redis(host='192.168.1.100',port=6379)

    def parse(self, response):
        dongchedi_video_ranking = 0
        dongchedi_article_ranking = 0
        
        li_list_video = response.xpath('//*[@id="__next"]/main/div/div/div[2]/section[1]/ul/li')
        li_list_article = response.xpath('//*[@id="__next"]/main/div/div/div[2]/section[2]/section/ul/li')
        
        for li in li_list_video:
            item = DongchediVideoItem()
            dongchedi_video_title = li.xpath('./a/span[2]/text()').extract_first()
            dongchedi_video_url = 'https://www.dongchedi.com' + li.xpath('./a/@href').extract_first()
            dongchedi_video_ranking = dongchedi_video_ranking + 1

            item['dongchedi_video_title'] = dongchedi_video_title
            item['dongchedi_video_url'] = dongchedi_video_url
            item['dongchedi_video_ranking'] = dongchedi_video_ranking

            ex = self.conn.sadd('dongchedi',dongchedi_video_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',dongchedi_video_url)
                yield item
            else:
                print('地址已经存在',dongchedi_video_url)
                yield item
        
        for li in li_list_article:
            item = DongchediArticleItem()

            dongchedi_article_title = li.xpath('./a/span[2]/text()').extract_first()
            dongchedi_article_url = 'https://www.dongchedi.com' + li.xpath('./a/@href').extract_first()
            dongchedi_article_ranking = dongchedi_article_ranking + 1

            item['dongchedi_article_ranking'] = dongchedi_article_ranking
            item['dongchedi_article_title'] = dongchedi_article_title
            item['dongchedi_article_url'] = dongchedi_article_url
            
            ex = self.conn.sadd('dongchedi',dongchedi_article_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',dongchedi_article_url)
                yield item
            else:
                print('地址已经存在',dongchedi_article_url)
                yield item




        


