'''
联系人设置页面
'''
from appium.webdriver.common.mobileby import MobileBy

from app.Page.base_page import BasePage
from app.Page.contactedit_page import ContactEditPage


class ContactDetailSettingPage(BasePage):
    def contact_remark(self):
        # 设置备注
        pass

    def recommended_to_contacts(self):
        # 推荐给联系人
        pass

    def set_star_contact(self):
        # 设为星标联系人
        pass

    def set_Attention(self):
        # 设为特别提醒
        pass

    def add_to_phone_addresslist(self):
        # 添加到手机通讯录
        pass

    def edit_number(self):
        # 编辑成员
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return ContactEditPage(self.driver)
