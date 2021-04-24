from redis import Redis
import os
import time
from datetime import datetime
from pathlib import Path

import re
def connect():

    host = '192.168.1.100'
    port = 6379
    conn = Redis(host=host,port=port)
    return conn

def add(conn,name,url):

    ex = conn.sadd(name,url)
    if ex==1:
        print('**该地址为新地址，可以进行任务获取',url)
        return True
    else:
        print('##地址已经存在',url)
        return False


def create_md(spider,item_dict):

    source_url = item_dict['source_url']
    title = item_dict['title']
    info_form = item_dict['info_form'] 
    shengzhu_type = item_dict['shengzhu_type'] 
    info_form = item_dict['info_form']
    today_date = info_form['today_date']
    yesterday_date = info_form['yesterday_date']

    fp = None
    dir_path = './today_data'
    save_path = Path(dir_path)
    # 创建文件夹
    if save_path.exists():
        pass
        #print('true')
    else:
        save_path.mkdir()


    name = title + '_'
    filename = name + datetime.today().strftime('%Y%m%d') + '.md'
    file_path = os.path.join(dir_path,filename)
    fp = open(file_path,'w',encoding='utf-8')
    fp.write('---')
    fp.write('\n')
    fp.write('title: %s'%(spider.name))
    fp.write('\n')
    ymd_time = time.strftime('%Y-%m-%d ',time.localtime())
    fp.write('date: %s'%(ymd_time))
    fp.write('\n')
    fp.write('tags: scrapy_%s'%(spider.name))
    fp.write('\n')
    fp.write('categories: news')
    fp.write('\n')
    fp.write('---')
    fp.write('\n')
    fp.write('# %s'%(shengzhu_type))
    fp.write('\n')
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fp.write('## %s'%(now_time))
    fp.write('\n')
    fp.write('## [数据源](%s)'%(source_url))
    fp.write('\n')
    fp.write('*****'+'\n')
    fp.write('| 省份 | %s | %s |'%(today_date,yesterday_date) + '\n')
    fp.write('| :----: | :----: | :----: |' + '\n')

    return fp

def test():

    title = '2021年04月23日全国外三元生猪价格行情涨跌表'
    ex = '(\d+)年(\d+)月(\d+)日全国(.*?)生猪价格'
    a = re.findall(ex,title)
    list_area = ['华东','西北','华中','华北','华南','东北','西南']
    td_1 = '华中1'
    

    full_date = '来源：中国养猪网 2021-04-23 07:30:25|  查看：次'
    ex = '(.*?)\|'
    str_re = re.findall(ex,full_date)
    
