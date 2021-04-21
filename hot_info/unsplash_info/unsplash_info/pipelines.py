# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.utils.project import get_project_settings
from unsplash_info.utils import create_md

import re
import os
from pathlib import Path
# md操作
class UnsplashInfoPipeline:

    fp = None
    project_settings = get_project_settings()
    image_path = project_settings.get('IMAGES_STORE')

    #重写父类方法，启动爬虫调用一次
    def open_spider(self,spider):

        self.fp = create_md(spider)
        save_path = Path(self.image_path)
        if not save_path.exists():
            print('****** 创建文件夹 image_path')
            save_path.mkdir()

    def process_item(self, item, spider):

        photo_id = item['photo_id']
        photo_url_small = item['photo_url_small']
        photo_user_id = item['photo_user_id']
        photo_user_name = item['photo_user_name']
        photo_user_html = item['photo_user_html']
        
        self.fp.write('![photo_url_small](%s)'%(photo_url_small))
        self.fp.write('\n')
        self.fp.write('- [%s - %s](%s)'%(photo_user_name,photo_id,photo_user_html))
        self.fp.write('\n')
        self.fp.write('\n')
        
        return item

    def close_spider(self,spider):
        #print('任务结束...')
        self.fp.close()

class imgPipeline(ImagesPipeline):
    
    project_settings = get_project_settings()
    image_path = project_settings.get('IMAGES_STORE')

    #发起对应图片路径的请求
    def get_media_requests(self, item, info):

        yield scrapy.Request(item['photo_url_small'])
    #指定图片存储的路径
    def file_path(self, request, response=None, info=None,item=None):
        
        url = item['photo_url_small']
        photo_user_name = item['photo_user_name']
        ex = 'photo-(.*?)\?crop'
        # 注意取出参数
        img_name = re.findall(ex,url,re.S)[0]
        save_path = os.path.join(self.image_path,photo_user_name)
        # 创建 根据用户名的 文件夹
        if not os.path.exists(save_path):
            os.mkdir(save_path)
            
        full_path = photo_user_name + '\\' + img_name + '.jpg'
        return full_path
        
    def item_completed(self, results, item, info):
        #返回到下一个执行的管道
        return item