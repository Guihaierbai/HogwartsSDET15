'''
邀请页面
'''
from appium.webdriver.common.mobileby import MobileBy

from app.Page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menual(self):
        # 点击手动输入添加
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from app.Page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result
