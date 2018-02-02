'''
@File: Common.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Website: https://touko.moe/
@Create at: 2018/1/29 17:10
@Desc: 
'''
import urllib
import urllib.request
import requests
import re
import os


class Web:
    @staticmethod
    def get_html(url):
        '''
        Get url from network
        :param url: Target url
        :return: result
        '''
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/55.0.2883.103 Safari/537.36'
        }
        try:
            response = requests.get(url, headers=headers).content
        except Exception as e:
            print(str(e))
            print('Direct connection failed, use proxy instead.')
            response = Web.get_html_by_proxy(url)
        return response

    @staticmethod
    def get_html_by_proxy(url):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/55.0.2883.103 Safari/537.36'
        }
        proxies = {
            "http": "http://127.0.0.1:1080",
            "https": "http://127.0.0.1:1080",
        }
        try:
            print('Get html by proxy.')
            response = requests.get(url, headers=headers, proxies=proxies).content
        except Exception as e:
            print(str(e))
            print('Proxy connection failed.')
            response = ''
        return response


class Text:
    def resolve_multi_line(text, newLineSymbol):
        '''
        A function to beautify text with meaningless multi blank line. The function will keep single line as it before, but merge multi blank line as 2.
        :param text: Original text
        :param newLineSymbol: The new line symbol, maybe "\n" or "\r\n"
        :return: Beautified text
        '''
        status = 0 # Status 0: refuse blank line; 1: accept one blank line; 2: wait for blank line.
        textList = text.split(newLineSymbol)
        newTextList = []
        for eachText in textList:
            # Pass spaces
            if eachText.isspace(): continue
            # Check
            if eachText != '':
                newTextList.append(eachText)
                status = 2
            else:
                if status == 1:
                    newTextList.append(eachText)
                    status = 0
                elif status == 2:
                    status = 1
        return newLineSymbol.join(newTextList)


    def get_between(s, start, end):
        return re.search('%s(.*)%s' % (start, end), s).group(1)

def down_img(imgurl, localpath):
    '''A function to save img'''
    if os.path.exists(localpath):
        print('%s exist!' % localpath)
        return
    print(imgurl, localpath)
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/55.0.2883.103 Safari/537.36'
    }
    request = urllib.request.Request(url=imgurl, headers=headers)
    data = urllib.request.urlopen(request).read()
    img_file = open(localpath, 'wb')
    img_file.write(data)
    img_file.close()
    return
