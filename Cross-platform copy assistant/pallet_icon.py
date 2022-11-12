import os
import pystray
import yaml
from PIL import Image
from pystray import MenuItem
# 加载本地函数
from tc import tc1, tc2
from copy_ import run_copy_


def click_menu(item):
    print("点击了", item)


def on_exit(icon):
    icon.stop()


def notify1(icon: pystray.Icon):
    icon.notify("已经启动，请复制想要发送的内容", "跨平台黏贴助手")
    run_copy_()
    icon.notify("已经发送内容至你的手机", "跨平台黏贴助手")


def notify_2(icon: pystray.Icon):
    run_copy_()
    icon.notify("已经发送内容至你的手机", "跨平台黏贴助手")


def notify_(icon: pystray.Icon):
    icon.notify("是右键我阿", "笨蛋！s(・｀ヘ´・;)ゞ")


def clipboard_get_time_notify1(icon):
    yamlPath = os.path.join("config\\config.yml")
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    params = yaml.load(cfg, Loader=yaml.SafeLoader)
    clipboard_get_time = params['clipboard_get_time']
    if clipboard_get_time:
        notify_2(icon)
    else:
        notify1(icon)


def clipboard_get_time_notify2():
    yamlPath = os.path.join("config\\config.yml")
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    params = yaml.load(cfg, Loader=yaml.SafeLoader)
    clipboard_get_time = params['clipboard_get_time']
    if clipboard_get_time:
        run_copy_()
        tc2()
    else:
        tc1()
        run_copy_()
        tc2()


# if __name__ == '__main__':
def backend_program():
    # 获取yaml文件路径
    yamlPath = os.path.join("config\\config.yml")
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    params = yaml.load(cfg, Loader=yaml.SafeLoader)
    print(params)
    left_switch = params['left_switch']
    print(left_switch)

    if left_switch:
        print('true')
        menu = (MenuItem(text='我是点击图标的菜单', action=clipboard_get_time_notify1, default=True, visible=False),
                MenuItem(text='发送复制内容', action=clipboard_get_time_notify1),
                MenuItem(text='', action=click_menu, enabled=False),
                MenuItem(text='切换点击图标模式', action=click_menu, enabled=False),
                MenuItem(text='', action=click_menu, enabled=False),
                MenuItem(text='退出', action=on_exit),
                )
        image = Image.open("icon\\copy_icon.png")
        icon = pystray.Icon("name", image, "快点击我吖！\n笨蛋！笨蛋！\ns(・｀ヘ´・;)ゞ", menu)
        icon.run()
    else:
        print('false')
        menu = (MenuItem(text='我是点击图标的菜单', action=notify_, default=True, visible=False),
                MenuItem(text='发送复制内容', action=clipboard_get_time_notify1),
                MenuItem(text='', action=click_menu, enabled=False),
                MenuItem(text='切换点击图标模式', action=click_menu, enabled=False),
                MenuItem(text='', action=click_menu, enabled=False),
                MenuItem(text='退出', action=on_exit),
                )
        image = Image.open("icon\\copy_icon.png")
        icon = pystray.Icon("name", image, "是右键啦！不是左键！！\n笨蛋！笨蛋！笨蛋！\ns(・｀ヘ´・;)ゞ", menu)
        icon.run()
