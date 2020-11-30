'''
基类模块：主要用来初始化driver，定义find，常用的基本方法
'''
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        print("self.driver=%s" % self.driver)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        return self.find(MobileBy.XPATH, "//*[@text='添加成功']").text
