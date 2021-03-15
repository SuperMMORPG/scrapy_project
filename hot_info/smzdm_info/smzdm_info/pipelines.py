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
class SmzdmInfoPipeline:
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
        self.fp.write('# smzdm')
        self.fp.write('\n')
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.fp.write('## %s'%(now_time))
        self.fp.write('\n')

    def process_item(self, item, spider):

        title = item['smzdm_title']
        url = item['smzdm_url']
        rank = item['smzdm_ranking']

        self.fp.write('1. [%s](%s)'%(title,url))
        self.fp.write('\n')

        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()

class mysqlSmzdmInfoPipeline(object):

    conn = None
    cursor = None
    def open_spider(self,spider):
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('准备连接数据库，开始smzdm任务...')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='*',db='scrapy_project',charset='utf8')

    def process_item(self, item, spider):

        self.cursor = self.conn.cursor()

        try:

            mysql_execute = 'INSERT INTO smzdm (ranking,url,title) VALUES ("%s","%s","%s");'
            url = item['smzdm_url']
            ranking = item['smzdm_ranking']
            title = item['smzdm_title']

            self.cursor.execute(mysql_execute,[ranking,url,title])
            self.conn.commit()

        except Exception as e:
            print('Mysql 抛出异常...')
            #print(item['title'])
            print(e)
            self.conn.rollback()
        
        return item
    
    def close_spider(self,spider):
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('数据库任务结束...')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        self.cursor.close()
        self.conn.close()
