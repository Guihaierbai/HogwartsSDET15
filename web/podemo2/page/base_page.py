# 基类 ： 最基本的方法，driver实例化，find（）等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver: WebDriver
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
