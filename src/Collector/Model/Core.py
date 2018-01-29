'''
@File: Core.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/29 16:24
@Desc: 
'''

import requests
from bs4 import BeautifulSoup


class Core(object):
    def __init__(self):
        self.name = 'Core'
        self.index = 'example.com'
        self.tasks = []

    def get_html(self, url):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/55.0.2883.103 Safari/537.36'
        }
        response = requests.get(url, headers=headers).content
        return response

    def save_data(self, data):
        print(data)

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            task()
