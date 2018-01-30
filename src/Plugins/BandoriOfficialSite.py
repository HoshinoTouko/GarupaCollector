'''
@File: BandoriOfficialSite.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/29 16:41
@Desc: 
'''

import urllib.parse as parse

from bs4 import BeautifulSoup
from src.Collector.Model import Common
from src.Collector.Model.DataBuffer import DataBuffer
from src.Collector.Model.Core import Core


class BandoriOfficialSite(Core):
    def __init__(self):
        super(BandoriOfficialSite, self).__init__()
        self.name = 'Bandori Official Site'
        self.index = 'https://bang-dream.com/'

        self.add_task(self.check_update)

    def check_update(self):
        response = self.get_html('https://bang-dream.com/update/')
        soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
        # Get articles
        articles = soup('article')
        # Foreach articles
        result = []
        i = 0
        for article in articles:
            i+=1
            if i > 4: break

            tmpData = DataBuffer()
            # Get simple data
            tmpData.set('title', article('h3')[0].get_text())
            tmpData.set('url', article('a')[0].attrs['href'])
            tmpData.set('desc', article('p')[0].get_text())
            tmpData.set('titleImg', article('img')[0].attrs['src'])
            tmpData.set('date', article.select('div span')[0].get_text())

            tmpData.set('content', '')
            tmpData.set('imgs', [])
            if True:
                # Get details
                try:
                    articleDetail = self.get_html(tmpData['url'])
                    detailSoup = BeautifulSoup(articleDetail, 'html.parser', from_encoding='utf-8')

                    tmpData.set(
                        'content',
                        Common.resolve_multi_line(
                            detailSoup('div', class_='in_post')[0].get_text(),
                            '\n'
                        )
                    )
                    imgs = detailSoup('div', class_='in_post')[0]('img')
                    tmpData.set(
                        'imgs',
                        list(map(lambda img: img.attrs['src'], imgs))
                    )
                except Exception as e:
                    tmpData.set('msg', 'Error: ' + str(e))
                else:
                    tmpData.set('msg', 'Success')
            result.append(tmpData.get_data())
        print(result)

if __name__ == '__main__':
    testPlugin = BandoriOfficialSite()
    testPlugin.run()
