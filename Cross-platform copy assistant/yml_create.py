#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from tkinter import messagebox
from img_decoding import mkdir

def yml_create():
    if os.path.exists('config\\config.yml'):
        print("配置文件已经生成")
        messagebox.showinfo(title='注意', message='跨平台黏贴助手已经启动，发送快捷键是CTRL+F1')
    else:
        mkdir('config')
        ret = \
            "#Bark配置\n" \
            "#填入你的推送设备id（例子：https://api.day.app/XJnSJLS2qdsaddztoKB/xxxxxxxxxxx    这里的设备id就是“XJnSJLS2qdsaddztoKB”）\n" \
            "ID : \n" \
            "#title_name是弹窗的标题\n" \
            "title_name : 跨平台黏贴助手\n" \
            "#content_name是弹窗的内容 ps：别太长别！带特殊字符！\n" \
            "content_name : 来自电脑的内容，长按弹窗可以复制内容\n" \
            "#grouping_name是消息分组\n" \
            "grouping_name : 跨平台黏贴助手\n" \
            "#icon_url是推送图标，建议400x400像素即可\n" \
            "icon_url : https://day.app/assets/images/avatar.jpg\n" \
            "#left_switch是管理击托盘图标是否启动程序（true & false）\n" \
            "left_switch : false\n" \
            "# clipboard_get_time是控制何时发送剪切板数据（true是及时发送，false是等待复制）\n"\
            "clipboard_get_time: true"

        savepath = "config\\config.yml"  # 保存的路径
        with open(savepath, "w", encoding="utf-8") as f:
            f.write(ret)
        # 弹窗提提示
        messagebox.showinfo(title='注意', message='配置文件已生成，请编辑配置文件并重启跨平台黏贴助手')



