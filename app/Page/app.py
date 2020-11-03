'''
app启动，重启，关闭等相关操作
'''
from appium import webdriver

from app.Page.base_page import BasePage
from app.Page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动APP
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
            # 保留缓存， 比如 登录
            caps['noReset'] = 'true'
            # 不停止APP， 直接执行用例
            caps['dontStopAppOnReset'] = 'true'
            caps['skipDeviceInitialization'] = 'true'
            caps['skipServerInstallation'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # 重启APP
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 关闭APP
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入首页
        return MainPage(self.driver)
