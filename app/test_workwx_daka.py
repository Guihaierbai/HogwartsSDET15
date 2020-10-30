from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWorkWx():
    def setup(self):
        caps = {}
        caps["platformName"] = 'android'
        caps["deviceName"] = '127.0.0.1.7555'
        caps["appPackage"] = 'com.tencent.wework'
        caps["appActivity"] = '.launch.WwMainActivity'
        caps["noReset"] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardwon(self):
        self.driver.quit()

    def test_workwx(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
