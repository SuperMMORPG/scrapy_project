# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from zhuwang_info.utils import create_md


class ZhuwangInfoPipeline:

    fp = None

    def process_item(self, item, spider):

        item_dict = item['item_dict']
        price_form = item_dict['info_form']['price_form']

        self.fp = create_md(spider,item_dict)
        for price_data in price_form:
            province_name = price_data['province_name']
            today_price = price_data['today_price']
            yesterday_price = price_data['yesterday_price']
            self.fp.write('| %s | %s | %s |'%(province_name,today_price,yesterday_price) + '\n')
        
        self.fp.write('*****'+'\n')

        self.fp.close()

        return item
    

