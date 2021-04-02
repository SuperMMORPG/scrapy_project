import scrapy
from scrapy.http import headers, request
from techcrunch_info.items import TechcrunchInfoItem

import requests

class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    urls = 'https://techcrunch.com/video/'

    def start_requests(self):

        HEADER = {
            'cookie': 'BX=c6e58q1g6dq24&b=3&s=ka; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://techcrunch.com/%22%2C%22sref%22:%22%22%2C%22sts%22:1617356863125%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=4685f6b1a7858ab977de6759fa02f747%22%2C%22session_count%22:1%2C%22last_session_ts%22:1617356863125}; cmp=t=1617356863&j=0; __gads=ID=d32b83ae0b90d636-22d4cd59f1c600dd:T=1617356871:RT=1617356871:S=ALNI_Ma6Hpt77xC2vavkPwRjQ6FyhjU7aA; rxx=2okc85yk964.2a7tx0le&v=1; _ga=GA1.2.963056395.1617356863; _gid=GA1.2.419694516.1617356865; __pnahc=0; __tbc=%7Bjzx%7DjGAToaZMxJYLoS7N4KRjDafn5XSpz0EcoSknZ3cFic6exb33ibBls8_N24t8_V3GKtuOcBQqgvFgOn733APUXA; __pat=-25200000; cX_S=kn04ipkmbi5l5ccn; A1=d=AQABBEXoZmACEKUXG2UitcK1I99IQqK_SmwFEgEBAwE0aGA8YSsNb2UB_eMAAAcIROhmYNCoOMM&S=AQAAArbGDo_JkYojD-b_4NSCHAY; A3=d=AQABBEXoZmACEKUXG2UitcK1I99IQqK_SmwFEgEBAwE0aGA8YSsNb2UB_eMAAAcIROhmYNCoOMM&S=AQAAArbGDo_JkYojD-b_4NSCHAY; A1S=d=AQABBEXoZmACEKUXG2UitcK1I99IQqK_SmwFEgEBAwE0aGA8YSsNb2UB_eMAAAcIROhmYNCoOMM&S=AQAAArbGDo_JkYojD-b_4NSCHAY&j=GDPR; GUC=AQEBAwFgaDRhPEIbzwPm; GUCS=AXOs2k8y; __pvi=%7B%22id%22%3A%22v-kn04ip3lba54t8uk%22%2C%22domain%22%3A%22.techcrunch.com%22%2C%22time%22%3A1617357545548%7D; xbc=%7Bjzx%7Di6XUW3DHrD_sAfJ0Kj64zY_cII2zD3PaR8zhxsH3bFIzIaWBVtvvVmUyGCuGqRZk1qpgTVkXVEzotudDxApqH6Aprjukih6wArZBt7ymmIkJNDZI0N8qWaSV8B4UmWM5GRfDhak2Ywc7lKYtk4tUZyFWF8-ZoN7ziDJRwkHm-9aPmhdh4-ZbZxS_4Tw4WWLyspNl9GJB1lI1LIy4vHOAgKaX4YivgsXBAW8N_X60P9cuuJ3wZEq4q7heNJp2KgmuQx4T1Xc8E1aSlC--aYMTBCkUf2ggh61ZACz0nHFBFx2mOAEli19OvGQQivDMImXexgeulxyAlQmfH59y4nZAOV7U6ShgyqfiLC1NCjUbGKtEleaUO7KNgeV38xSdJlg24z24sJBt2_9wO2-KW3iSwPOehTSUweTR5pBOcHn1VAd3gqTNPskBIH1b6G4lu1p-HM3ste3P31E91I3_tJ5GqyLFQ_vgb5pLh9HNrxCDgDuxG7C2qYWmOKnN5Yos_2LmgQbkEHXQzv6-RPdGcetEOT2BWSTzn3BwVImusSbRQmouP6AwbqtwFZXcTQ0dkYhG1DlijtIal7yJ8GJFSv_2HqlqQgVTSFdcQzFYenNCW-7mXsYdGThNmdVuL3nEcJUEcNeLYHYcUYvKqaEXnybtxh5b-6vaB1Dy89ST9vXnoltSFi_qJK3MfJuWHPtQ3XRk9eSvXn7IGILOlayKMpsKmmjCMO2YbZ9lAEGrEZ97hRY',
        }
        
        yield scrapy.Request(self.urls,callback=self.parse,headers=HEADER)

    def parse(self, response):

        # 解析页面xpath路径 或者 解析scripts的json
        article_list = response.xpath('//*[@class="post-block__header"]')
        #print(article_list)

        for article in article_list:
            url = article.xpath('./h2/a/@href').extract_first()
            title = article.xpath('./h2/a/text()').extract_first().strip()
            content = article.xpath('./div[1]/text()').extract_first().strip()
            author = article.xpath('.//span/a/text()').extract_first().strip()
            up_date = article.xpath('.//time/@datetime').extract_first()

            item = TechcrunchInfoItem()
            item['url'] = url
            item['title'] = title
            item['content'] = content
            item['author'] = author
            item['up_date'] = up_date

            yield item

