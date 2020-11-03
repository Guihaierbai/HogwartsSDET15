'''
成员编辑页
'''
from appium.webdriver.common.mobileby import MobileBy

from app.Page.addresslist_page import AddressListPage
from app.Page.base_page import BasePage


class ContactEditPage(BasePage):
    def delete_contact(self):
        # 删除成员
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        return AddressListPage(self.driver)
