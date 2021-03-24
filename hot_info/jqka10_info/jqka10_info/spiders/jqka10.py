import scrapy
from jqka10_info.items import Jqka10InfoItem
from redis import Redis
class Jqka10Spider(scrapy.Spider):
    name = 'jqka10'
    conn = Redis(host='192.168.1.100',port=6379)

    #start_urls = ('http://q.10jqka.com.cn/index/index/board/all/field/zd/order/desc/page/%d/ajax/1/' % i for i in range(1,6))
    start_urls = ('http://q.10jqka.com.cn/index/index/board/all/field/zd/order/desc/page/%d/ajax/1/'% i for i in range(1,3))
    
    def start_requests(self):
        # 指定cookies

        '''    '''
        cookies ={
            'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1':'1616577960',
            '__utma':'156575163.463470466.1616577976.1616577976.1616577976.1',
            '__utmc':'156575163',
            '__utmz':'156575163.1616577976.1.1.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/',
            'Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1':'1616579368',
            'v':'AwrZXU9sXh65WdKy3Le8dxxOW_uv-47kgH8C95RDtt3oR6StfIveZVAPUlxn', # 这个值变化
        }

        for url in self.start_urls:
            # 请求，可以去试试声明回调函数callback，dont_filter=True 不进行域名过滤，meta给回调函数传递数据
            yield scrapy.Request(url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        #print(response.status)
        #print(response.body_as_unicode())  #查看url
        tr_list = response.xpath('//tr')
        if not tr_list:
            print('********************************')
            print('数据为空，估计cookies过期')
            print('********************************')
        
        n = 0
        for tr in tr_list:

            if n == 0:
                n = n + 1
                continue

            ranking = tr.xpath('./td[1]/text()').extract_first()
            code = tr.xpath('./td[2]/a/text()').extract_first()
            name = tr.xpath('./td[3]/a/text()').extract_first()
            up_and_down = tr.xpath('./td[6]/text()').extract_first()
            url = tr.xpath('./td[2]/a/@href').extract_first()

            item = Jqka10InfoItem()
            item['ranking'] = ranking
            item['code'] = code
            item['name'] = name
            item['up_and_down'] = up_and_down
            item['url'] = url

            ex = self.conn.sadd('10jqka',url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item