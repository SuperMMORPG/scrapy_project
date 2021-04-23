# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from zhuwang_info.utils import create_md

# 此markdown文件 格式不满意 待修改
class ZhuwangInfoPipeline:
    fp = None

    #重写父类方法，启动爬虫调用一次
    def open_spider(self,spider):
        
        self.fp = create_md(spider)

    def process_item(self, item, spider):

        province_name = item['province_name']
        today_price = item['today_price']
        yesterday_price = item['yesterday_price']
        source_url = item['source_url']
        title = item['title']
        today_date = item['today_date']
        yesterday_date = item['yesterday_date']
        shengzhu_type = item['shengzhu_type']

        self.fp.write('| %s | %s | %s |'%(province_name,today_price,yesterday_price))

        self.fp.write('\n')
        
        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()
