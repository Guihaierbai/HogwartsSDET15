'''
app启动，重启，关闭等相关操作
'''
from app.Page.main_page import MainPage


class App:
    def start(self):
        # 启动APP
        return self

    def restart(self):
        # 重启APP
        pass

    def stop(self):
        # 关闭APP
        pass

    def goto_main(self) -> MainPage:
        # 进入首页
        return MainPage()
