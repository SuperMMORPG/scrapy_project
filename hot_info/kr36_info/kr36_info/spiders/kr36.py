import scrapy
from kr36_info.items import Kr36RenqiItem,Kr36ZongheItem,Kr36ShoucangItem


class Kr36Spider(scrapy.Spider):
    name = 'kr36'
    start_urls = ['https://36kr.com/hot-list/catalog']

    def getInfo(self, div):
        
        ranking = 0
        info_dict = {}
        div_list = div.xpath('./div[2]/div')
        for d in div_list:
            info_list = []
            url = 'https://36kr.com' + d.xpath('./div/div/div/div[2]/p/a/@href').extract_first()
            title = d.xpath('./div/div/div/div[2]/p/a/text()').extract_first()
            ranking = ranking + 1
            info_list.append(title)
            info_list.append(url)

            info_dict[ranking] = info_list
        
        return info_dict

    def parse(self, response):

        div_list = response.xpath('//*[@id="app"]/div/div[1]/div[3]/div/div/div[2]/div[1]/div')
        div_renqi = div_list[0]
        div_zonghe = div_list[1]
        div_shoucang = div_list[2]

        renqi_dict = self.getInfo(div_renqi)
        for d in renqi_dict:
            item = Kr36RenqiItem()
            info_list = renqi_dict[d]

            item['renqi_ranking'] = d
            item['renqi_title'] = info_list[0]
            item['renqi_url'] = info_list[1]
            yield item
        
        zonghe_dict = self.getInfo(div_zonghe)
        for d in zonghe_dict:
            item = Kr36ZongheItem()
            info_list = zonghe_dict[d]

            item['zonghe_ranking'] = d
            item['zonghe_title'] = info_list[0]
            item['zonghe_url'] = info_list[1]
            yield item
        
        shoucang_dict = self.getInfo(div_shoucang)
        for d in shoucang_dict:
            item = Kr36ShoucangItem()
            info_list = shoucang_dict[d]

            item['shoucang_ranking'] = d
            item['shoucang_title'] = info_list[0]
            item['shoucang_url'] = info_list[1]
            yield item

        


        
        



        