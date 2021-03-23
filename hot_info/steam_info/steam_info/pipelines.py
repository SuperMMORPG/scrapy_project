# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import time
from datetime import datetime

class SteamInfoPipeline:
    fp = None
    #重写父类方法，启动爬虫调用一次
    def open_spider(self,spider):
        #print('开始任务...')

        dir_path = './today_data'
        name = spider.name + '_'
        filename = name + datetime.today().strftime('%Y%m%d') + '.md'
        file_path = os.path.join(dir_path,filename)
        self.fp = open(file_path,'w',encoding='utf-8')
        self.fp.write('---')
        self.fp.write('\n')
        self.fp.write('title: %s'%(spider.name))
        self.fp.write('\n')
        ymd_time = time.strftime('%Y-%m-%d ',time.localtime())
        self.fp.write('date: %s'%(ymd_time))
        self.fp.write('\n')
        self.fp.write('tags: scrapy_%s'%(spider.name))
        self.fp.write('\n')
        self.fp.write('categories: news')
        self.fp.write('\n')
        self.fp.write('---')
        self.fp.write('\n')
        self.fp.write('# steam')
        self.fp.write('\n')
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.fp.write('## %s'%(now_time))
        self.fp.write('\n')

        self.fp.write('### 热销商品'+'\n')
        self.fp.write('******'+'\n')

    def process_item(self, item, spider):

        name = item['name']
        url = item['url']
        price = item['price']
        rank = item['ranking']
        release_date = item['release_date']

        self.fp.write('1. [%s](%s) ¥ %s'%(name,url,price))
        self.fp.write('\n')

        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()
