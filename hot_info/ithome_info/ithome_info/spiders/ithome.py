import scrapy
from redis import Redis

from ithome_info.items import IthomeInfoItem

class IthomeSpider(scrapy.Spider):
    name = 'ithome'

    start_urls = ['https://www.ithome.com/']
    conn = Redis(host='192.168.1.100',port=6379)

    def getInfo(self,li_list,ithome_time):

        info_dict = {}
        ithome_ranking = 0

        for li in li_list:

            info_list = []

            ithome_url = li.xpath('./a/@href').extract_first()
            ithome_title = li.xpath('./a/text()').extract_first()
            ithome_ranking = ithome_ranking + 1
            info_list.append(ithome_url)
            info_list.append(ithome_title)
            info_list.append(ithome_time)
            
            info_dict[ithome_ranking] = info_list

        return info_dict

    def parse(self, response):

        #li_day_list = response.xpath('//*[@id="d-1"]/li')
        #li_week_list = response.xpath('//*[@id="d-2"]/li')
        #li_month_list = response.xpath('//*[@id="d-3"]/li')
        ul_list = response.xpath('//*[@id="rank"]/ul')
        li_day_list = ul_list[1].xpath('./li')
        li_week_list = ul_list[2].xpath('./li')
        li_month_list = ul_list[3].xpath('./li')

        info_dict = self.getInfo(li_day_list,'ithome_day')
        for d in info_dict:

            item = IthomeInfoItem()
            item['ithome_url'] = info_dict[d][0]
            item['ithome_title'] = info_dict[d][1]
            item['ithome_ranking'] = d
            item['ithome_time'] = info_dict[d][2]

            ex = self.conn.sadd('ithome',info_dict[d][0])
            if ex==1:
                print('该地址为新地址，可以进行任务获取',info_dict[d][0])
                yield item
            else:
                print('地址已经存在',info_dict[d][0])
                yield item
        
        info_dict = self.getInfo(li_week_list,'ithome_week')
        for d in info_dict:

            item = IthomeInfoItem()
            item['ithome_url'] = info_dict[d][0]
            item['ithome_title'] = info_dict[d][1]
            item['ithome_ranking'] = d
            item['ithome_time'] = info_dict[d][2]

            ex = self.conn.sadd('ithome',info_dict[d][0])
            if ex==1:
                print('该地址为新地址，可以进行任务获取',info_dict[d][0])
                yield item
            else:
                print('地址已经存在',info_dict[d][0])
                yield item
        
        info_dict = self.getInfo(li_month_list,'ithome_month')
        for d in info_dict:

            item = IthomeInfoItem()
            item['ithome_url'] = info_dict[d][0]
            item['ithome_title'] = info_dict[d][1]
            item['ithome_ranking'] = d
            item['ithome_time'] = info_dict[d][2]

            ex = self.conn.sadd('ithome',info_dict[d][0])
            if ex==1:
                print('该地址为新地址，可以进行任务获取',info_dict[d][0])
                yield item
            else:
                print('地址已经存在',info_dict[d][0])
                yield item
        


        
        



