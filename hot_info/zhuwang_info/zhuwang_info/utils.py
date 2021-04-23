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


def create_md(spider):

    #print('开始任务...')
    fp = None
    dir_path = './today_data'

    save_path = Path(dir_path)

    if save_path.exists():
        pass
        #print('true')
    else:
        save_path.mkdir()


    name = spider.name + '_'
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
    fp.write('# %s'%(spider.name))
    fp.write('\n')
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fp.write('## %s'%(now_time))
    fp.write('\n')
    fp.write('*****'+'\n')
    fp.write('| 省份 | 今日 | 昨日 |' + '\n')
    fp.write('| :----: | :----: | :----: |' + '\n')

    return fp

def test():

    title = '2021年04月23日全国外三元生猪价格行情涨跌表'
    ex = '(\d+)年(\d+)月(\d+)日全国(.*?)生猪价格'
    a = re.findall(ex,title)
    list_area = ['华东','西北','华中','华北','华南','东北','西南']
    td_1 = '华中1'
    if td_1 in list_area:
        print(td_1)
