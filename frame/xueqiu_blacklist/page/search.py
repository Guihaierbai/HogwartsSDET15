from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from frame.xueqiu_blacklist.page.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find(MobileBy.XPATH, '//*[@resource-id = "com.xueqiu.android:id/search_input_text"]').send_keys('alibaba')
        self.parse_yaml("../page/search.yml", "search")
