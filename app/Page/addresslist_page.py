# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.Page.base_page import BasePage

from app.Page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_addnumber(self):
        # 滚动查找点击添加成员
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def click_number(self, name):
        # 滚动查找点击成员
        self.find_by_scroll(name).click()
        from app.Page.contactdetail_page import ContactDetailPage
        return ContactDetailPage(self.driver)
