import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1. 打开雪球app
        2. 点击搜索输入框
        3. 想搜索输入框里输入“阿里巴巴”
        4. 在搜索结果里面选择“阿里巴巴”，然后进行点击
        5. 获取阿里巴巴的股价并判断这只股票的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text = '阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    def test_attr(self):
        """
        打开雪球应用首页
        定位首页搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name'and @text = '阿里巴巴']")
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()


if __name__ == '__main__':
    pytest.main()
