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
            tmpData = {}
            # Get simple data
            tmpData['title'] = article('h3')[0].get_text()
            tmpData['url'] = article('a')[0].attrs['href']
            tmpData['desc'] = article('p')[0].get_text()
            tmpData['titleImg'] = article('img')[0].attrs['src']
            tmpData['date'] = article.select('div span')[0].get_text()

            tmpData['content'] = ''
            tmpData['imgs'] = []
            if True:
                # Get details
                try:
                    articleDetail = self.get_html(tmpData['url'])
                    detailSoup = BeautifulSoup(articleDetail, 'html.parser', from_encoding='utf-8')

                    tmpData['content'] = detailSoup('div', class_='in_post')[0].get_text()
                    tmpData['content'] = Common.resolve_multi_line(tmpData['content'], '\n')
                    imgs = detailSoup('div', class_='in_post')[0]('img')
                    for img in imgs:
                        tmpData['imgs'].append(img.attrs['src'])
                except Exception as e:
                    tmpData['msg'] = 'Error: ' + str(e)
                else:
                    tmpData['msg'] = 'Success'
            result.append(tmpData)
        print(result)

if __name__ == '__main__':
    testPlugin = BandoriOfficialSite()
    testPlugin.run()
