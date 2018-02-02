'''
@File: Public.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/2/2 12:58
@Desc: 
'''
import json
from flask import Blueprint
from src import Config

Public = Blueprint('public', __name__)


@Public.route('/get_plugin_name')
def get_plugin_name():
    plugins = Config.activePlugins
    pluginNameList = list(map(lambda plugin: plugin.tag, plugins))
    result = {
        'code': 200,
        'result': pluginNameList
    }
    return json.dumps(result, ensure_ascii=False)


@Public.route('/data/<pluginName>')
def get_data_by_plugin_name(pluginName):
    plugins = Config.activePlugins
    pluginMap = dict(zip(
        map(lambda plugin: plugin.tag, plugins),
        plugins
    ))
    data = pluginMap[pluginName].load_data()
    result = {
        'code': 200,
        'result': data
    }
    return json.dumps(result, ensure_ascii=False)
