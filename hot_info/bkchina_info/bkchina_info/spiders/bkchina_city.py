import scrapy
import re
from bkchina_info.items import BkchinaInfoItem

class BkchinaCitySpider(scrapy.Spider):
    name = 'bkchina_city'
    start_urls = ['https://www.bkchina.cn/restaurant/index.html']

    url = 'https://www.bkchina.cn/restaurant/getStoreCity?storeCity={cityname}' 

    def getCityName(self,li_list):
        '''
        得到地区下的所有城市名称
        param:li_list li标签
        return:city 城市名称列表
        '''
        city = []
        for li in li_list:
            
            city_name = li.xpath('./a/text()').extract_first()
            city.append(city_name)

        return city

    def parse(self, response):

        div_list = response.xpath('/html/body/div/div[5]/div/div/div')

        for div in div_list:
            area = {}
            area_name = div.xpath('./i/text()').extract_first()
            li_list = div.xpath('./ul/li')
            city_list = self.getCityName(li_list)
            #area[area_name] = city_list

            for city in city_list:

                item = BkchinaInfoItem()
                item['area_name'] = area_name
                item['city'] = city
                city_url = self.url.format(cityname=city)
                # city != None
                if city:
                    yield scrapy.Request(url=city_url,callback=self.parse_detail,meta={'item':item})
                else:
                    pass

    def parse_detail(self,response):

        item = response.meta['item']
        text = response.xpath('/html/body/div/div/li[1]/a/text()').extract_first()
        store_num = re.findall(r'\d+',text)
        # 提取店数
        item['store_num'] = store_num[0]
        # 去掉 符号 :
        item['area_name'] = item['area_name'][:-1]

        yield item


