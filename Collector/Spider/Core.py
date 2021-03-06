'''
@File: Core.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/29 16:24
@Desc: 
'''
import re

from Collector.Spider.Database import Database
from Collector.Spider.DataBuffer import DataBuffer


class Core(object):

    def __init__(
            self,
            name='Default',
            index='example.com',
            tag='Default',
            desc='Default desc',
            tableName='Default'
    ):
        self.name = name
        self.index = index
        self.tag = tag
        self.desc = desc
        self.tableName = tableName
        self.task_map = []
        self.parser_map = {}

    def task(self, f):
        self.task_map.append(f)
        return f

    # Read and write
    def save_data(self, data):
        # print(data)
        Database.get_db().insert(self.tableName, data)

    def load_data(self):
        data = Database.get_db().select(self.tableName)
        # print(data)
        return data

    # Parser
    def parse(self, url, buffer=DataBuffer()):
        for pattern in self.parser_map.keys():
            if re.match(pattern, url):
                print('Use: %s, parse: %s' % (pattern, url))
                return self.parser_map.get(pattern)(url, buffer)
        print('Use: %s, parse: %s' % ('default', url))
        return self.parser_map.get('default')(url, buffer)

    def parser(self, pattern):
        def add_parser(f):
            if isinstance(pattern, list):
                for item in pattern:
                    self.parser_map[item] = f
            else:
                self.parser_map[pattern] = f
            return f
        return add_parser

    def get_parser(self):
        return self.parser_map

    # Tasks
    def add_task(self, task):
        self.task_map.append(task)

    def run(self):
        for task in self.task_map:
            task()


if __name__ == '__main__':
    core = Core()
    print(core.parser_map)

