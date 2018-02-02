'''
@File: BandoriOfficialSite.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/29 16:41
@Desc: 
'''
import time

from bs4 import BeautifulSoup
from Collector.Spider.Common import Web, Text
from Collector.Spider.DataBuffer import DataBuffer
from Collector.Spider.Core import Core
from Collector.Spider.Database import Database

from multiprocessing import Pool

BandoriOfficialSite = Core(
    name='Bandori Official Site',
    index='http://bang-dream.com/',
    tag='bos',
    tableName='BandoriOfficialSite'
)


@BandoriOfficialSite.task
def check_update():
    # Old url list
    oldUrlList = list(map(lambda item: item['url'], BandoriOfficialSite.load_data()))
    # Get articles
    maxPage = 1
    articles = []
    for currentPage in range(maxPage):
        url = 'https://bang-dream.com/update/page/%s' % (currentPage+1)
        print('Visiting...: %s' % url)
        response = Web.get_html(url)
        soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
        articles += soup('article')
    # Foreach articles
    tmpResult = []
    # Reverse articles
    articles.reverse()
    # Iter articles
    maxId = Database.get_db().find_max(BandoriOfficialSite.tableName, 'id') + 1
    for article in articles:
        tmpData = DataBuffer()
        # Get simple data
        try:
            tmpData.set('title', article('h3')[0].get_text())
        except Exception as e:
            print(str(e))

        url = article('a')[0].attrs['href']
        tmpData.set('url', url)

        tmpData.set('desc', article('p')[0].get_text())
        try:
            tmpData.set('titleImg', article('img')[0].attrs['src'])
        except Exception as e:
            print(str(e))

        try:
            unixTime = time.strptime(
                article.select('div span')[0].get_text().strip() + ' 12:00',
                '%Y/%m/%d %H:%M'
            )
            tmpData.set('time', time.mktime(unixTime))
        except Exception as e:
            print(e)

        tmpData.set('content', '')
        tmpData.set('imgs', [])

        # Add to result
        if url not in oldUrlList:
            tmpData.set('id', maxId)
            maxId += 1
            tmpResult.append(tmpData)

    print(tmpResult)

    # Get details
    pool = Pool(10)
    result = pool.map(
        get_details,
        tmpResult
    )
    print(result)
    BandoriOfficialSite.save_data(result)


def get_details(item):
    return BandoriOfficialSite.parse(item['url'], item).get_data()

@BandoriOfficialSite.parser([
    '^https://bang-dream.com/news/',
    '^https://bang-dream.com/cd/',
    '^https://bang-dream.com/interview/',
    '^https://bang-dream.com/event/',
    '^https://bang-dream.com/goods/'
    '^https://bang-dream.com/'
])
def common_parser(url, buffer):
    try:
        articleDetail = Web.get_html(url)
        detailSoup = BeautifulSoup(articleDetail, 'html.parser', from_encoding='utf-8')

        buffer.set('content', Text.resolve_multi_line(
            detailSoup('div', class_='in_post')[0].get_text(),
            '\n'
        ))

        imgs = detailSoup('div', class_='in_post')[0]('img')
        if len(imgs) != 0:
            buffer.set('imgs', list(map(lambda img: img.attrs['src'], imgs)))
    except Exception as e:
        buffer.set('msg', 'Error: ' + str(e))
    else:
        buffer.set('msg', 'Success')
    return buffer


@BandoriOfficialSite.parser([
    '^https://bang-dream.com/character/'
])
def character_parser(url, buffer):
    try:
        articleDetail = Web.get_html(url)
        detailSoup = BeautifulSoup(articleDetail, 'html.parser', from_encoding='utf-8')

        buffer.set('content', Text.resolve_multi_line(
            detailSoup('div', id='contents')[0].get_text(),
            '\n'
        ))

        imgs = detailSoup('div', id='contents')[0]('img')
        if len(imgs) != 0:
            buffer.set('imgs', list(map(lambda img: img.attrs['src'], imgs)))
    except Exception as e:
        buffer.set('msg', 'Error: ' + str(e))
    else:
        buffer.set('msg', 'Success')
    return buffer


@BandoriOfficialSite.parser([
    '^https://www.youtube.com/',
    '^goo.gl',
    '^https://youtu.be/'
])
def proxy_parser(url, buffer):
    try:
        articleDetail = Web.get_html_by_proxy(url)
        detailSoup = BeautifulSoup(articleDetail, 'html.parser', from_encoding='utf-8')

        buffer.set('content', Text.resolve_multi_line(
            detailSoup('div', id='meta')[0].get_text(),
            '\n'
        ))

        imgs = detailSoup('body')[0]('img')
        if len(imgs) != 0:
            buffer.set('imgs', list(map(lambda img: img.attrs['src'], imgs)))
    except Exception as e:
        buffer.set('msg', 'Error: ' + str(e))
    else:
        buffer.set('msg', 'Success')
    return buffer


@BandoriOfficialSite.parser('default')
def default_parser(url, buffer):
    try:
        articleDetail = Web.get_html(url)
        detailSoup = BeautifulSoup(articleDetail, 'html.parser', from_encoding='utf-8')

        buffer.set('content', Text.resolve_multi_line(
            detailSoup('body')[0].get_text(),
            '\n'
        ))

        imgs = detailSoup('body')[0]('img')
        if len(imgs) != 0:
            buffer.set('imgs', list(map(lambda img: img.attrs['src'], imgs)))
    except Exception as e:
        buffer.set('msg', 'Error: ' + str(e))
    else:
        buffer.set('msg', 'Success')
    return buffer


if __name__ == '__main__':
    BandoriOfficialSite.run()
