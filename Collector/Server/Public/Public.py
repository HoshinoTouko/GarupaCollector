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
import os
from flask import Blueprint, request, jsonify, render_template
from src import Config
from Collector.Common import Data

Public = Blueprint('public', __name__)

@Public.route('/get_plugin_name')
def get_plugin_name():
    plugins = Config.activePlugins
    pluginNameList = list(map(lambda plugin: {
        'name': plugin.name,
        'index': plugin.index,
        'desc': plugin.desc,
        'tag': plugin.tag
    }, plugins))
    result = {
        'code': 200,
        'result': pluginNameList
    }
    return Data.jsonify(result)


@Public.route('/data/<pluginName>', methods=['GET'])
def get_data_by_plugin_name(pluginName):
    # Get page and num
    if not request.args.get('page'):
        page = 1
    else:
        page = int(request.args.get('page'))
    if not request.args.get('num'):
        num = 10
    else:
        num = int(request.args.get('num'))
    # Get active plugins
    plugins = Config.activePlugins
    pluginMap = dict(zip(
        map(lambda plugin: plugin.tag, plugins),
        plugins
    ))
    try:
        data = []
        if pluginName == 'all':
            for plugin in pluginMap.values():
                data += plugin.load_data()
        else:
            data = pluginMap[pluginName].load_data()
        data, page, total, totalPage = Data.data_filter(
            data,
            page = page,
            num = num
        )
        code = 1
        msg = 'Success'
    except Exception as e:
        data = []
        code = -1
        msg = str(e)
        page, total, totalPage = 0, 0, 0
    result = {
        'code': code,
        'result': data,
        'msg': msg,
        'page' : page,
        'total': total,
        'totalPage': totalPage
    }
    return Data.jsonify(result)
