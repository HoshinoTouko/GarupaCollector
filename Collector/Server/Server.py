'''
@File: Server.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/2/2 12:52
@Desc: 
'''
from flask import Flask
from Collector.Server.Public.Public import Public

APP = Flask(__name__)

APP.register_blueprint(Public, url_prefix='/public')

if __name__ == '__main__':
    APP.run()
