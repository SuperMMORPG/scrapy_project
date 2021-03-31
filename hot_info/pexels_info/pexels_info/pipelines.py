# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pexels_info.utils import create_md
class PexelsInfoPipeline:

    fp = None

    #重写父类方法，启动爬虫调用一次
    def open_spider(self,spider):

        self.fp = create_md(spider)

    def process_item(self, item, spider):

        name = item['name']
        url = item['url']
        ranking = item['name']

        self.fp.write('- [ %s ](%s)'%(name,url))
        self.fp.write('\n')
        
        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()