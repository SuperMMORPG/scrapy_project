# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import bkchina_info.utils as db
from bkchina_info.items import BkchinaInfoItem,BkchinaStoreItem

class BkchinaInfoPipeline:

    conn = None
    cursor = None

    def open_spider(self,spider):
        '''
        连接数据库
        '''
        self.conn = db.connection
        self.cursor = self.conn.cursor()

    def get_areaId_by_areaName(self,item):
        '''
        通过area_name得到area_id
        '''
        area_name = item['area_name']
        mysql_execute = "SELECT id FROM area WHERE area_name='%s'" % area_name
        self.cursor.execute(mysql_execute)
        try:
            id = self.cursor.fetchone()['id']
            return id
        except Exception as e:
            print(e)
            print('Warning:area_id  没拿到')
            return False

    def get_cityId_by_cityName(self,item):

        city = item['city']
        mysql_execute = "SELECT id FROM city WHERE city_name='%s'" % city
        self.cursor.execute(mysql_execute)
        try:
            id = self.cursor.fetchone()['id']
            return id
        except Exception as e:
            print(e)
            print('city_id 不存在')
            return False

    def save_city_data(self,item):
        '''
        保存city表数据
        '''
        try:

            mysql_execute = 'INSERT INTO city (city_name,area_id,store_num) VALUES (%s,"%s","%s");'
            area_id = int(item['area_id'])
            city = item['city']
            store_num = int(item['store_num'])

            self.cursor.execute(mysql_execute,[city,area_id,store_num])
            self.conn.commit()
            print('****** save,success',city)
            return True

        except Exception as e:
            print('Warning:save_city_data###',item)
            #print('Mysql 抛出异常...')
            print(e)
            self.conn.rollback()
            return False

    def updata_city_data(self,item):
        '''
        更新city表数据
        '''
        try:
            area_id = int(item['area_id'])
            city = item['city']
            store_num = int(item['store_num'])
            city_id = item['city_id']

            mysql_execute = "UPDATE city SET city_name=%s,area_id=%s,store_num=%s WHERE id=%s"
            self.cursor.execute(mysql_execute,[city,area_id,store_num,city_id])
            self.conn.commit()
            print('&&&&& updata,success',city)
            return True

        except Exception as e:
            print('Warning: updata_city_data###',item)
            #print('Mysql 抛出异常...')
            print(e)
            self.conn.rollback()
            return False
    
    def save_store_data(self,item):
        '''
        保存store表数据
        '''
        try:

            mysql_execute = 'INSERT INTO store (city_id,store_name,store_address,store_tel,store_opening_hours) VALUES (%s,%s,%s,%s,%s);'
            
            city_id = item['city_id']
            store_name = item['store_name']
            store_address = item['store_address']
            store_tel = item['store_tel']
            store_opening_hours = item['store_opening_hours']

            self.cursor.execute(mysql_execute,[city_id,store_name,store_address,store_tel,store_opening_hours])
            self.conn.commit()
            print('****** save store,success',store_name)
            return True

        except Exception as e:
            print('Warning:save_store_data###',item)
            #print('Mysql 抛出异常...')
            print(e)
            self.conn.rollback()
            return False

    def process_item(self, item, spider):

        if isinstance(item,BkchinaInfoItem):
            #先查city是否存在数据
            city_id = self.get_cityId_by_cityName(item)
            area_id = self.get_areaId_by_areaName(item)
            if not city_id:
                if area_id:
                    item['area_id'] = area_id
                    self.save_city_data(item)
                else:
                    print('area_id 不存在')
            else:
                if area_id:
                    item['city_id'] = int(city_id)
                    item['area_id'] = area_id
                    self.updata_city_data(item)
                else:
                    print('area_id 不存在')

        elif isinstance(item,BkchinaStoreItem):
            # 存数据
            self.save_store_data(item)

        return item
    
    def close_spider(self,spider):
        print('数据库任务结束...')
        self.cursor.close()
        self.conn.close()
