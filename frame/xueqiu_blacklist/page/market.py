'''
搜索页
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from frame.xueqiu_blacklist.page.base_page import BasePage
from frame.xueqiu_blacklist.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # print("goto_search")
        # 点击进入搜索页
        # self.find(MobileBy.XPATH, '//*[@resource-id = "com.xueqiu.android:id/action_search"]').click()
        self.parse_yaml("../page/market.yml", "goto_search")
        return Search(self.driver)
