import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re
from zhuwang_info.items import ZhuwangInfoItem
class ZhuwangSpider(CrawlSpider):
    name = 'zhuwang'
    start_urls = ['https://hangqing.zhuwang.cc/shengzhu/index.html']

    #https://hangqing.zhuwang.cc/shengzhu/20210423/468708.html
    link = LinkExtractor(allow=r'shengzhu/\d+/\d+.html',restrict_xpaths=('//div[@class="zxleft3"]/ul/li/p[@class="zxleft31"]/a'))
    
    rules = (
        Rule(link, callback='parse_details', follow=False),
    )

    def parse_details(self, response):

        source_url = response.url
        list_area = ['华东','西北','华中','华北','华南','东北','西南']
        title = response.xpath('/html/body/div[4]/div[1]/div[1]/p[1]/text()').extract_first()
        today_date = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/table/thead/tr/th[3]').extract_first()
        yesterday_date = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/table/thead/tr/th[4]').extract_first()
        #2021年04月01日全国外三元生猪价格行情涨跌表
        ex = '(\d+)年(\d+)月(\d+)日全国(.*?)生猪价格'
        re_text = re.findall(ex,title)
        info_year = re_text[0][0]
        info_month = re_text[0][1]
        info_month = re_text[0][2]
        # 生猪页面的不同类型
        shengzhu_type = re_text[0][3]
        
        tr_list = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/table//tr')
        for tr in tr_list:
            td_1 = tr.xpath('./td[1]/text()').extract_first()
            if td_1 == None:
                continue
            if td_1 in list_area:
                province_name = tr.xpath('./td[2]/text()').extract_first()
                today_price = tr.xpath('./td[3]/text()').extract_first()
                yesterday_price = tr.xpath('./td[4]/text()').extract_first()
            else:
                province_name = tr.xpath('./td[1]/text()').extract_first()
                today_price = tr.xpath('./td[2]/text()').extract_first()
                yesterday_price = tr.xpath('./td[3]/text()').extract_first()
        
            item = ZhuwangInfoItem()
            item['source_url'] = source_url
            item['title'] = title
            item['today_date'] = today_date
            item['yesterday_date'] = yesterday_date
            item['province_name'] = province_name
            item['today_price'] = today_price
            item['yesterday_price'] = yesterday_price
            item['shengzhu_type'] = shengzhu_type
            yield item




