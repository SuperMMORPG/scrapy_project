# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from picrew_info.utils import create_md

class PicrewInfoPipeline:
    fp = None
    #重写父类方法，启动爬虫调用一次
    def open_spider(self,spider):

        self.fp = create_md(spider)

    def process_item(self, item, spider):

        title = item['title']
        url = item['url']
        creator = item['creator']
        avatar_url = item['avatar_url']

        self.fp.write('![avatar_url](%s)'%(avatar_url))
        self.fp.write('\n')
        self.fp.write('- [%s - %s](%s)'%(title,creator,url))
        self.fp.write('\n')
        self.fp.write('\n')
        
        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()
