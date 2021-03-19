# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import os
import time
from datetime import datetime

from dongchedi_info.items import DongchediInfoItem,DongchediVideoItem,DongchediArticleItem

class DongchediInfoPipeline:
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
        self.fp.write('# dongchedi')
        self.fp.write('\n')
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.fp.write('## %s'%(now_time))
        self.fp.write('\n')
        self.fp.write('******'+'\n')
        self.fp.write('### 视频排行榜'+'\n')

    def process_item(self, item, spider):

        if isinstance(item,DongchediVideoItem):

            title = item['dongchedi_video_title']
            url = item['dongchedi_video_url']
            rank = item['dongchedi_video_ranking']

            self.fp.write('1. [%s](%s)'%(title,url))
            self.fp.write('\n')


            return item

        if isinstance(item,DongchediArticleItem):

            if item['dongchedi_article_ranking'] == 1:
                self.fp.write('******'+'\n')
                self.fp.write('### 文章排行榜'+'\n')
            title = item['dongchedi_article_title']
            url = item['dongchedi_article_url']

            self.fp.write('1. [%s](%s)'%(title,url))
            self.fp.write('\n')

            return item

        
    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()
