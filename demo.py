# coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4


def gethtml(url, headers):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            print('抓取成功网页长度：', len(response.text))
            response.encoding = 'utf-8'
            return response.text
    except BaseException as e:
        print('抓取出现错误：', e)


def getsoup(html):
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.find('tbody').children:  # 生成tr的tag列表
        if isinstance(tr, bs4.element.Tag):
            td = tr('td')  # 循环获取所有tr标签下的td标签，并生成tag列表
            t = [td[0].string, td[1].string, '', td[2].string, '', td[3].string]  # 提取前四td字符串
            list.append(t)


def write_data(list):
    for i in list:  # 循环提取list中的元素
        with open('daxue.txt', 'a') as  data:
            print(i, file=data)  # 写入文件


if __name__ == '__main__':
    list = []
    url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    html = gethtml(url, headers)
    getsoup(html)
    print(list)
    # write_data(list)

