#!/usr/bin/python
# vim: set file encoding:utf-8
import os
from tkinter import messagebox

import yaml
import pyperclip
from urllib.parse import quote
import urllib.request
import urllib
import time

"""<<<<--------------延迟等待获取剪切板-------------->>>>"""


# 获取剪切板，稳定不出错
class niubi():
    def lihai(self):
        while True:
            # jianting().main()
            t = jianting().main()
            # print(t)


class jianting():
    def clipboard_get(self):
        """获取剪贴板数据"""
        data = pyperclip.paste()  # 主要这里差别
        return data

    def main(self):
        """后台脚本：每隔0.2秒，读取剪切板文本，检查有无指定字符或字符串，如果有则执行替换"""
        # recent_txt 存放最近一次剪切板文本，初始化值只多执行一次paste函数读取和替换
        recent_txt = self.clipboard_get()
        while True:
            # txt 存放当前剪切板文本
            txt = self.clipboard_get()
            # 剪切板内容和上一次对比如有变动，再进行内容判断，判断后如果发现有指定字符在其中的话，再执行替换
            if txt != recent_txt:
                # print(f'txt:{txt}')
                recent_txt = txt  # 没查到要替换的子串，返回None
                return recent_txt

                # 检测间隔（延迟0.2秒）
            time.sleep(0.2)


"""<<<<--------------及时获取剪切板-------------->>>>"""


def clipboard_get_instant():
    # 获取剪贴板数据
    data = pyperclip.paste()
    print(data)
    return data


def run_copy_():
    # 获取yml文件路径
    yamlPath = os.path.join("config\\config.yml")
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    params = yaml.load(cfg, Loader=yaml.SafeLoader)
    print(params)
    # 读取配置文件config.yml
    ID = params['ID']
    title_name = params['title_name']
    content_name = params['content_name']
    grouping_name = params['grouping_name']
    icon_url = params['icon_url']
    clipboard_get_time = params['clipboard_get_time']

    print(ID)
    print(title_name)
    print(content_name)
    print(grouping_name)
    print(icon_url)
    print(clipboard_get_time)

    if clipboard_get_time:
        # 及时获取剪切板
        contents_name = clipboard_get_instant()
    else:
        # 延迟获取剪切板
        contents_name = jianting().main()

    # 将剪切板字符进行url编码
    contents_url_code_name = urllib.parse.quote(contents_name)
    print(contents_url_code_name)
    # 将题目进行url编码
    title_url_code_name = urllib.parse.quote(title_name)
    print(title_url_code_name)
    # 将内容进行url编码
    content_url_code_name = urllib.parse.quote(content_name)
    print(content_url_code_name)
    # 将消息分组进行url编码
    grouping_url_code_name = urllib.parse.quote(grouping_name)
    print(grouping_url_code_name)

    try:
        # 访问合成后的网址
        url = 'https://api.day.app/' + ID + '/' + title_url_code_name + '/' + content_url_code_name + '?icon=' + icon_url + '&group=' + grouping_url_code_name + '&copy=' + contents_url_code_name + '&isArchive=0'
        print(url)
        response = urllib.request.urlopen(url)
        string = response.read()
        html = string.decode('utf-8')
        print(html)
    except:
        messagebox.showinfo(title='注意！！！', message='config配置文件出错，请检查')


# if __name__ == '__main__':
#     run_copy_()
