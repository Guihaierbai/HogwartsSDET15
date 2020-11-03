'''
联系人个人信息页
'''
from appium.webdriver.common.mobileby import MobileBy

from app.Page.base_page import BasePage
from app.Page.contactdetail_setting_page import ContactDetailSettingPage


class ContactDetailPage(BasePage):
    def invite_number(self):
        # 邀请成员
        pass

    def send_message(self):
        # 发信息
        pass

    def voice_calls(self):
        # 语音通话
        pass

    def contact_setting(self):
        # 更多
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxm')
        return ContactDetailSettingPage(self.driver)
