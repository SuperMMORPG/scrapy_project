import scrapy

from picrew_info.items import PicrewInfoItem
class PicrewSpider(scrapy.Spider):
    name = 'picrew'
    start_urls = ('https://picrew.me/search?s=2&page=%d' % i for i in range(1,6))

    def parse(self, response):

        li_list = response.xpath('//li[@class="search-ImagemakerList_Result"]')
        for li in li_list:
            url = 'https://picrew.me' + li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/div[2]/div[1]/text()').extract()
            title = "".join(title).strip()
            creator = li.xpath('./a/div[2]/div[2]/text()').extract_first()
            avatar_url = li.xpath('./a/div[1]/@data-bg').extract_first()
            item = PicrewInfoItem()
            item['url'] = url
            item['title'] = title
            item['creator'] = creator
            item['avatar_url'] = avatar_url
            yield item



