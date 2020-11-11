import yaml
from appium.webdriver.common.mobileby import MobileBy

from frame.xueqiu_blacklist.page.base_page import BasePage
from frame.xueqiu_blacklist.page.market import Market


class MainPage(BasePage):

    def goto_market(self):
        # print("goto_market")
        # 制造假弹框
        # self.find(MobileBy.XPATH, '//*[@resource-id = "com.xueqiu.android:id/post_status"]').click()
        # 点击行情
        # self.find(MobileBy.XPATH, '//*[@resource-id = "android:id/tabs"]//*[@text="行情"]').click()
        # with open("./mainpage.yml", 'r', encoding='utf-8') as f:
        #     data = yaml.load(f)
        # steps = data['goto_market']
        # # 遍历steps里的step
        # for step in steps:
        #     if 'click' == step['action']:
        #         self.find(step['by'], step['locator']).click()
        self.parse_yaml("../page/mainpage.yml", "goto_market")
        return Market(self.driver)
