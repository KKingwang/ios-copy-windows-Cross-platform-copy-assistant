import base64
from copy_icon_png import img as one  # 引入img变量，赋别名为one
from copy_icon_ico import img as two


def mkdir(path):
    '''
    创建指定的文件夹
    :param path: 文件夹路径，字符串格式
    :return: True(新建成功) or False(文件夹已存在，新建失败)
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def copy_icon_png_decoding():
    mkdir('icon')
    tmp = open('icon\\copy_icon.png', 'wb')  # 创建临时的文件
    tmp.write(base64.b64decode(one))  # 把这个one图片解码出来，写入文件中去。
    tmp.close()


def copy_icon_ico_decoding():
    mkdir('icon')
    tmp = open('icon\\copy_icon.ico', 'wb')  # 创建临时的文件
    tmp.write(base64.b64decode(two))  # 把这个one图片解码出来，写入文件中去。
    tmp.close()

# 这个放在代码最后，如果放在前面，会马上删除图片，导致程序不能正常运行
# copy_icon_png_decoding()
# copy_icon_ico_decoding()
# os.remove('icon\\copy_icon.png')  # 用完可以删除这个临时图片
# os.remove('icon\\copy_icon.ico')  # 用完可以删除这个临时图片
