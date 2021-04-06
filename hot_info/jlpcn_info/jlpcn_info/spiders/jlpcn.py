import scrapy
import re
from scrapy.http import request
from jlpcn_info.items import JlpcnInfoItem

class JlpcnSpider(scrapy.Spider):
    name = 'jlpcn'
    start_urls = ['http://www.jlpcn.net/']

    def parse(self, response):
        li_list = response.xpath('//*[@id="tv"]/div/div[2]/div/div[2]/ul/li')
        #num = 0
        for li in li_list:
            #num = num + 1
            url = 'http://www.jlpcn.net' + li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/text()').extract_first()

            item = JlpcnInfoItem()
            item['url'] = url
            item['title'] = title
            
            yield scrapy.Request(url,callback=self.detail_parse,meta={'item':item})
        
    def detail_parse(self,response):

        item = response.meta['item']
        english_title = response.xpath('/html/body/div[7]/div[1]/div/div[1]/div/div[3]/ul/li[1]/span/text()').extract_first()
        ul_list = response.xpath('//*[@id="down_list_2"]/ul')
        print(item['url'])
        bt_all = []
        for ul in ul_list:
            bt_dl = []
            bt_url = ul.xpath('./li/script/text()').extract_first()

            regex = r"\+\(\"(.*)\"\)\+"
            bt_url_re = re.findall(regex,bt_url)
            br_url_new = bt_url_re[0].replace('\\',"")
            #print(br_url_new)
            
            '''
            matches = re.finditer(regex, bt_url, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
            '''

            bt_name = ul.xpath('./li/p/strong/text()').extract_first()
            bt_dl.append(br_url_new)
            bt_dl.append(bt_name)
            bt_all.append(bt_dl)
        
        item['bt_all'] = bt_all
        yield item

            