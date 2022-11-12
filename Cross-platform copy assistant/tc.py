from plyer import notification


def tc1():
    notification.notify(title='跨平台黏贴助手',
                        message='已经启动，请复制想要发送的内容',
                        app_icon="icon\\copy_icon.ico",
                        )


def tc2():
    notification.notify(title='跨平台黏贴助手',
                        message='已经发送内容至你的手机',
                        app_icon="icon\\copy_icon.ico",
                        )
