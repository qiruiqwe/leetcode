# @Time : 2020/11/22 17:21
# @Author : 亓瑞
# @File : 数据爬取.py
# @desc :
# 一、爬取百度百科中《平凡的荣耀》中所有演员信息，返回页面数据

import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os
import lxml


# 一、爬取百度百科中《平凡的荣耀》中所有演员信息，返回页面数据
def crawl_wiki_data():
    """
    爬取百度百科中《平凡的荣耀》中演员信息，返回html
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    url = 'https://baike.baidu.com/item/平凡的荣耀'

    try:
        response = requests.get(url, headers=headers)
        # 将一段文档传入BeautifulSoup的构造方法,就能得到一个文档的对象, 可以传入一段字符串
        soup = BeautifulSoup(response.text, 'lxml')
        # 返回class="lemmaWgt-roleIntroduction"的div,即“角色介绍”下方的div
        roleIntroductions = soup.find('div', {'class': 'lemmaWgt-roleIntroduction'})
        all_roleIntroductions = roleIntroductions.find_all('li')
        actors = []
        for every_roleIntroduction in all_roleIntroductions:
            actor = {}
            if every_roleIntroduction.find('div', {'class': 'role-actor'}):
                # 找演员名称和演员百度百科连接
                actor["name"] = every_roleIntroduction.find('div', {'class': 'role-actor'}).find('a').text
                actor['link'] = 'https://baike.baidu.com' + every_roleIntroduction.find('div',
                                                                                        {'class': 'role-actor'}).find(
                    'a').get('href')
            actors.append(actor)
    except Exception as e:
        print(e)

    json_data = json.loads(str(actors).replace("\'", "\""))
    cwd = os.getcwd()
    with open(cwd + '\work\\' + 'actors.json', 'w', encoding='UTF-8') as f:
        json.dump(json_data, f, ensure_ascii=False)


# 二、爬取每个演员的百度百科页面的信息，并进行保存
def crawl_everyone_wiki_urls():
    '''
    爬取每个演员的百度百科图片，并保存
    '''
    with open('work/' + 'actors.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36 '
    }
    actor_infos = []
    for star in json_array:
        actor_info = {}
        name = star['name']
        link = star['link']
        actor_info['name'] = name
        # 向演员个人百度百科发送一个http get请求
        response = requests.get(link, headers=headers)
        # 将一段文档传入BeautifulSoup的构造方法,就能得到一个文档的对象
        bs = BeautifulSoup(response.text, 'lxml')
        # 获取演员的民族、星座、血型、体重等信息
        base_info_div = bs.find('div', {'class': 'basic-info cmn-clearfix'})
        dls = base_info_div.find_all('dl')
        for dl in dls:
            dts = dl.find_all('dt')
            for dt in dts:
                if "".join(str(dt.text).split()) == '民族':
                    actor_info['nation'] = dt.find_next('dd').text
                if "".join(str(dt.text).split()) == '星座':
                    actor_info['constellation'] = dt.find_next('dd').text
                if "".join(str(dt.text).split()) == '血型':
                    actor_info['blood_type'] = dt.find_next('dd').text
                if "".join(str(dt.text).split()) == '身高':
                    height_str = str(dt.find_next('dd').text)
                    actor_info['height'] = str(height_str[0:height_str.rfind('cm')]).replace("\n", "")
                if "".join(str(dt.text).split()) == '体重':
                    actor_info['weight'] = str(dt.find_next('dd').text).replace("\n", "")
                if "".join(str(dt.text).split()) == '出生日期':
                    birth_day_str = str(dt.find_next('dd').text).replace("\n", "")
                    if '年' in birth_day_str:
                        actor_info['birth_day'] = birth_day_str[0:birth_day_str.rfind('年')]
        actor_infos.append(actor_info)
        # 将演员个人信息存储到json文件中
        json_data = json.loads(str(actor_infos).replace("\'", "\""))
        with open('work/' + 'actor_infos.json', 'w', encoding='UTF-8') as f:
            json.dump(json_data, f, ensure_ascii=False)


# 三、爬取《平凡的荣耀》的收视情况，并保存
def crawl_viewing_data():
    """
    爬取百度百科中《平凡的荣耀》收视情况，返回html
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    url = 'https://baike.baidu.com/item/平凡的荣耀'

    try:
        response = requests.get(url, headers=headers)
        # 将一段文档传入BeautifulSoup的构造方法,就能得到一个文档的对象, 可以传入一段字符串
        soup = BeautifulSoup(response.text, 'lxml')

        # 返回所有的<table>所有标签
        tables = soup.find_all('table')
        crawl_table_title = "收视情况"
        for table in tables:
            # 对当前节点前面的标签和字符串进行查找
            table_titles = table.find_previous('div')
            for title in table_titles:
                if (crawl_table_title in title):
                    return table
    except Exception as e:
        print(e)


def parse_viewing_data(viewing_table):
    """
    对《平凡的荣耀》的收视情况table进行解析，并保存
    """
    viewing_datas = []

    trs = viewing_table.find_all('tr')

    for i in range(len(trs)):
        if i < 2:
            continue
        viewing_data = {}
        tds = trs[i].find_all('td')
        viewing_data["broadcastDate"]= tds[0].text
        viewing_data["dongfang_rating"]= tds[1].text
        viewing_data["dongfang_rating_share"]= tds[2].text
        viewing_data["dongfang_ranking"]= tds[3].text
        viewing_data["zhejiang_rating"]= tds[4].text
        viewing_data["zhejiang_rating_share"]= tds[5].text
        viewing_data["zhejiang_ranking"]= tds[6].text
        viewing_datas.append(viewing_data)
    #将个人信息存储到json文件中
    json_data = json.loads(str(viewing_datas).replace("\'","\""))
    with open('work/' + 'viewing_infos.json', 'w', encoding='UTF-8') as f:
        json.dump(json_data, f, ensure_ascii=False)

if __name__ == '__main__':
    # 爬取百度百科中《平凡的荣耀》中演员信息，返回html
    crawl_wiki_data()

    # 爬取每个演员的信息,并保存
    crawl_everyone_wiki_urls()

    # 1.爬取百度百科中《平凡的荣耀》收视情况，返回html
    # 2、对《平凡的荣耀》的收视情况table进行解析，并保存
    viewing_table = crawl_viewing_data()
    parse_viewing_data(viewing_table)

