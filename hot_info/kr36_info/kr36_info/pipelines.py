# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import time
from datetime import datetime

from kr36_info.items import Kr36RenqiItem,Kr36ZongheItem,Kr36ShoucangItem
class Kr36InfoPipeline:
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
        self.fp.write('# 36Kr')
        self.fp.write('\n')
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.fp.write('## %s'%(now_time))
        self.fp.write('\n')

    def process_item(self, item, spider):

        if isinstance(item,Kr36RenqiItem):

            title = item['renqi_title']
            url = item['renqi_url']
            rank = item['renqi_ranking']
            if rank == 1:
                self.fp.write('### 人气榜' + '\n')
                self.fp.write('******')
                self.fp.write('\n')
            self.fp.write('1. [%s](%s)'%(title,url))
            self.fp.write('\n')
        
        if isinstance(item,Kr36ZongheItem):

            title = item['zonghe_title']
            url = item['zonghe_url']
            rank = item['zonghe_ranking']
            if rank == 1:
                self.fp.write('### 综合榜' + '\n')
                self.fp.write('******')
                self.fp.write('\n')
            self.fp.write('1. [%s](%s)'%(title,url))
            self.fp.write('\n')
        
        if isinstance(item,Kr36ShoucangItem):

            title = item['shoucang_title']
            url = item['shoucang_url']
            rank = item['shoucang_ranking']
            if rank == 1:
                self.fp.write('### 收藏榜' + '\n')
                self.fp.write('******')
                self.fp.write('\n')
            self.fp.write('1. [%s](%s)'%(title,url))
            self.fp.write('\n')
        
        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()
