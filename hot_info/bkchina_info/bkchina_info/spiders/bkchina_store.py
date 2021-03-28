import scrapy

import bkchina_info.utils as db
from bkchina_info.items import BkchinaStoreItem

class BkchinaStoreSpider(scrapy.Spider):
    name = 'bkchina_store'
    start_urls = 'https://www.bkchina.cn/restaurant/getStoreCity?storeCity={cityName}&p={page}'

    conn = None
    cursor = None

    def get_all_city(self):
        '''
        得到所有的city信息
        '''
        mysql_execute = "SELECT * FROM city;"
        self.cursor.execute(mysql_execute)
        try:
            city = self.cursor.fetchall()
            return city
        except Exception as e:
            print(e)
            print('Warning:City  没拿到')
            return False

    def start_requests(self):
        '''
        连接数据库，并发起request路径请求
        '''
        self.conn = db.connection
        self.cursor = self.conn.cursor()

        all_city = self.get_all_city()
        for city in all_city:
            
            item = BkchinaStoreItem()
            item['city_id'] = city['id']
            item['city_name'] = city['city_name']
            item['store_num'] = city['store_num']

            # 根据页数区分请求
            if item['store_num'] > 100:
                for page in range(1,4):
                    url = self.start_urls.format(cityName=item['city_name'],page=page)
                    yield scrapy.Request(url,callback=self.parse,meta={'item':item})
            elif item['store_num'] <= 100 and item['store_num'] > 50:
                for page in range(1,3):
                    url = self.start_urls.format(cityName=item['city_name'],page=page)
                    yield scrapy.Request(url,callback=self.parse,meta={'item':item})
            else:
                url = self.start_urls.format(cityName=item['city_name'],page=1)
                yield scrapy.Request(url,callback=self.parse,meta={'item':item})
    
    def getStoreInfo(self,li_list):
        '''
        得到页面的店铺信息
        param: li_list li标签
        return: all_shop 页面的所有店铺列表
        '''
        all_shop = []
        for li in li_list:
            #单个店铺信息
            shop = []
            shop_name = li.xpath('./dl/dd[1]/text()').extract_first()
            shop_address = li.xpath('./dl/dd[2]/text()').extract_first()
            shop_tel = li.xpath('./dl/dd[3]/text()').extract_first()
            shop_time = li.xpath('./dl/dd[4]/text()').extract_first()
            shop.append(shop_name)
            shop.append(shop_address)
            shop.append(shop_tel)
            shop.append(shop_time)

            all_shop.append(shop)
        return all_shop

    def parse(self, response):

        item = response.meta['item']

        li_list = response.xpath('/html/body/div/ul/li')
        all_shop = self.getStoreInfo(li_list)
        for shop in all_shop:
            item['store_name'] = shop[0]
            item['store_opening_hours'] = shop[3]
            item['store_address'] = shop[1]
            item['store_tel'] = shop[2]

            yield item