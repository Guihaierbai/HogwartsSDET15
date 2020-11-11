import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from frame.xueqiu_blacklist.page.handle_black import handle_black


class BasePage:
    black_list = [(MobileBy.XPATH, '//*[@resource-id = "com.xueqiu.android:id/iv_close"]')]

    # 声明driver类型为WebDriver
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        # print("find_self.driver=%s" %self.driver)
        # try:
        if locator is None:
            # 如果传的元素是一个，只有by
            return self.driver.find_element(*by)
        else:
            # 如果传的元素是2个，既有by又有locator
            return self.driver.find_element(by, locator)

        # #如果有异常弹窗导致无法找到元素，进入黑名单逻辑
        # except Exception as e:
        #     # 将黑名单中的元素存放到black_ele中
        #     for black_ele in self.black_list:
        #         # 查找页面中是否存在黑名单中的元素并存放到list ele中
        #         ele = self.driver.find_elements(*black_ele)
        #         # 如果ele的长度大于0，说明找到了黑名单中的元素
        #         if len(ele) > 0:
        #             # 点击黑名单中的第一个元素
        #             ele[0].click()
        #             # 处理完黑名单后再次查找原来的元素
        #             return self.find(by, locator)
        #     raise e

    def parse_yaml(self, path, func_name):
        """
        读取 yaml ，取出关键数据，用 parse 进行解析
        :param path:
        :param func_name:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        """
        解析 yaml　内容
        :param steps:
        :return:
        """
        # 遍历每一个步骤
        for step in steps:
            # 如果是点击
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            # 如果是发送内容
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step["content"])
