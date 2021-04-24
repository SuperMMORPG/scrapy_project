import json
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
    # 限制了一下页数
    #link_page = LinkExtractor(allow=r'list-63-([0-9]|(1[0-5])).html',attrs=('href'))
    link_page = LinkExtractor(allow=r'list-63-[1-2].html',attrs=('href'))
    rules = (
        Rule(link, callback='parse_details', follow=False),
        Rule(link_page,callback='parse_page',follow=True),
    )

    def parse_page(self,response):

        source_url = response.url
        print(source_url)

    def parse_details(self, response):

        source_url = response.url
        list_area = ['华东','西北','华中','华北','华南','东北','西南']
        title = response.xpath('/html/body/div[4]/div[1]/div[1]/p[1]/text()').extract_first()
        today_date = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/table/thead/tr/th[3]/text()').extract_first()
        yesterday_date = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/table/thead/tr/th[4]/text()').extract_first()
        #2021年04月01日全国外三元生猪价格行情涨跌表
        ex = '(\d+)年(\d+)月(\d+)日全国(.*?)生猪价格'
        re_text = re.findall(ex,title)
        info_year = re_text[0][0]
        info_month = re_text[0][1]
        info_day = re_text[0][2]
        # 生猪页面的不同类型
        shengzhu_type = re_text[0][3]
        # 得到完整日期
        get_full_date = response.xpath('/html/body/div[4]/div[1]/div[1]/text()').extract()
        full_date = "".join(get_full_date).strip()
        ex = '(.*?)\|'
        full_date_list = re.findall(ex,full_date)
        full_date = full_date_list[0]

        # 字典数据
        item_dict = {}
        # 一级数据
        item_dict['source_url'] = source_url
        item_dict['title'] = title
        item_dict['info_form'] = {'today_date':today_date,'yesterday_date':yesterday_date}
        item_dict['info_date'] = [info_year,info_month,info_day,full_date] #发布日期 年月日 完整日期
        item_dict['shengzhu_type'] = shengzhu_type

        tr_list = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/table//tr')
        item = ZhuwangInfoItem()
        item_list = []
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
            # 二级数据
            price_data = {}
            price_data['province_name'] = province_name
            price_data['today_price'] = today_price
            price_data['yesterday_price'] = yesterday_price
            item_list.append(price_data)
        
        item_dict['info_form']['price_form'] = item_list

        item['item_dict'] = item_dict
        
        yield item




