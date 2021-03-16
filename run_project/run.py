#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from time import sleep
import redis

'''
得到需要运行的文件位置
返回路径和名称
'''
def getDirPath():
    #当前路径
    current_path = os.path.join(os.getcwd(),'hot_info')
    #得到文件夹名称列表
    list_dir_name = os.listdir(current_path)
    list_name = []
    list_dir_path = []
    #循环各个文件路径
    for dir_name in list_dir_name:
        dir_path = os.path.join(current_path,dir_name)
        list_dir_path.append(dir_path)
        #切割文件夹名称
        list_split_name = dir_name.split('_')
        name = list_split_name[0]
        #避免有多个版本的脚本
        if len(list_split_name) == 3:
            name = list_split_name[0] + list_split_name[2]
        
        list_name.append(name)
        #print(dir_path)
        #print(list_dir_path)

    return list_dir_path,list_name

def getRedisStatus():

    conn = redis.Redis(host='127.0.0.1',port=6379)
    try:
        status = conn.ping()
        if status:
            print('redis server running......')
            return True
    except redis.exceptions.ConnectionError:
        print('No Redis Server')
        return False
    

#运行各个脚本
def run(list_dir_path,list_name):

    status = getRedisStatus()
    if not status:
        print('********************')
        return False

    for (dir_path,name) in zip(list_dir_path,list_name):

        #修改当前工作目录
        os.chdir( dir_path )
        #查看修改后的工作目录
        #retval = os.getcwd()
        #print ("******修改后工作目录为 %s" % retval)
        sleep(2)
        ex = 'scrapy crawl ' + name
        os.system(ex)
        print('***********************')
        print('运行 %s 结束'%(name))
        print('***********************')
        sleep(5)

#测试
def test():

    os.chdir('./hot_info\\bilibili_info')
    print(os.getcwd())

def run_copy():

    return None

if __name__ == '__main__':

    #getRedisStatus()

    list_result= getDirPath()
    run(list_result[0],list_result[1])
    #test()
