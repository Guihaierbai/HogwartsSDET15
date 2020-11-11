from appium import webdriver

from frame.xueqiu_blacklist.page.base_page import BasePage
from frame.xueqiu_blacklist.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        # 启动APP
        if self.driver == None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.xueqiu.android'
            caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
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
        self.driver.quit()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # print("goto_main self.driver%s" %self.driver)
        return MainPage(self.driver)
