'''
@File: BandoriOfficialSite.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/29 16:41
@Desc: 
'''

from bs4 import BeautifulSoup
from Collector.Common import Web, Text
from Collector.DataBuffer import DataBuffer
from Collector.Core import Core

from multiprocessing import Pool

BandoriOfficialSite = Core(name='Bandori Official Site', index='http://bang-dream.com/')


@BandoriOfficialSite.task
def check_update():
    response = Web.get_html('https://bang-dream.com/update/')
    soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
    # Get articles
    articles = soup('article')
    # Foreach articles
    tmpResult = []
    result = []
    i = 0
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
        tmpData.set('date', article.select('div span')[0].get_text())

        tmpData.set('content', '')
        tmpData.set('imgs', [])

        # Add to result
        tmpResult.append(tmpData)

    print(tmpResult)
    # Get details
    pool = Pool(8)
    result = pool.map(
        get_details,
        tmpResult
    )
    print(result)


def get_details(item):
    return BandoriOfficialSite.parse(item['url'], item).get_data()

@BandoriOfficialSite.parser([
    '^https://bang-dream.com/news/',
    '^https://bang-dream.com/cd/'
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
    '^https://www.youtube.com/',
    'https://youtu.be/'
])
def common_parser(url, buffer):
    try:
        articleDetail = Web.get_html(url)
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
def common_parser(url, buffer):
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
