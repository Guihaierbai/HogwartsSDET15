'''
首页
'''
from appium.webdriver.common.mobileby import MobileBy

from app.Page.addresslist_page import AddressListPage
from app.Page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    address_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_message(self):
        # 进入消息页
        pass

    def goto_address(self):
        # 进入通讯录页
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)
