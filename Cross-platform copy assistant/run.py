import os
import threading
from yml_create import yml_create
from pallet_icon import backend_program
from global_hotkeys import main
from img_decoding import copy_icon_ico_decoding, copy_icon_png_decoding

if __name__ == '__main__':
    # 运行初始化程序
    copy_icon_ico_decoding()
    copy_icon_png_decoding()
    yml_create()
    # 创建全局快捷键后台的线程
    global_hotkeys_run_thread = threading.Thread(target=main, daemon=True)
    # 开启子线程
    global_hotkeys_run_thread.start()
    # 开启主线程
    backend_program()
    os.remove('icon\\copy_icon.png')  # 用完可以删除这个临时图片
    os.remove('icon\\copy_icon.ico')  # 用完可以删除这个临时图片

