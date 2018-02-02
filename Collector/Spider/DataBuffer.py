'''
@File: DataBuffer.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/30 15:51
@Desc: 
'''
class DataBuffer(object):
    def __init__(self):
        self.__dict__ = {
            'title': '',
            'url': '',
            'desc': '',
            'titleImg': '',
            'time': 0,
            'content': '',
            'imgs': [],
            'msg': 'Null'
        }

    def set(self, key, value):
        self.__dict__[key] = value

    def is_success(self):
        return self.__dict__.get('msg') == 'Success'

    def get_data(self):
        return self.__dict__

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __cmp__(self, other):
        keyTable = ['title', 'url', 'desc', 'titleImg', 'date']
        for key in keyTable:
            if self.__dict__.get(key) != other.data.get(key):
                return False
        return True

    def __set__(self, instance, value):
        self.__dict__ = value

    def __get__(self, instance, owner):
        return self.__dict__
