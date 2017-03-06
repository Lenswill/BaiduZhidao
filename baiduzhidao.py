#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/3/5 18:51
# @Author  : Wilson
# @Version : 0.8

#导入库文件
import requests
from bs4 import BeautifulSoup
import time
import re


#网络请求的请求头
# headers = {
#         'User-Agent': '',
#         'cookie': ''
#         }


#构造爬取函数
def get_page(url,data=None):

    #获取URL的requests
    wb_data = requests.get(url)
    wb_data.encoding = ('gbk')
    soup = BeautifulSoup(wb_data.text,'lxml')

    #定义爬取的数据
    titles = soup.select('a.ti')
    answer_times = soup.select('dd.dd.explain.f-light > span:nth-of-type(1)')
    answer_users = soup.select('dd.dd.explain.f-light > span:nth-of-type(2) > a')
    answers = soup.select('dd.dd.explain.f-light > span:nth-of-type(3) > a')
    agrees = soup.select('dd.dd.explain.f-light > span.ml-10.f-black')
    # agrees.encoding = ('gbk')

    #在获取到的数据提取有效内容
    if data==None:
        for title,answer_time,answer_user,answer,agree in zip(titles,answer_times,answer_users,answers,agrees):
            data = [
                title.get_text(),
                answer_time.get_text(),
                answer_user.get_text(),
                answer.get_text(),
                agree.get_text()
            ]
            print(data)
            # saveFile(data)

#迭代页数
def get_more_page(start,end):
    for one in range(start,end,10):
        get_page(url+str(one))
        time.sleep(2)

#定义保存文件函数
def saveFile(data):
    path = "/Users/Wilson/Desktop/1233.txt"
    file = open(path,'a')
    file.write(str(data))
    file.write('\n')
    file.close()

#主体
#定义爬取关键词、页数
keyword = input('请输入关键词\n')
pages = input('请输入页码\n')

#定义将要爬取的URL
url = 'https://zhidao.baidu.com/search?word=' + keyword + '&ie=gbk&site=-1&sites=0&date=0&pn='

#开始爬取
get_more_page(0,int(pages)*10)