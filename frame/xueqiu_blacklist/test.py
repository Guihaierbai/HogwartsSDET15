import time

from appium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 保留缓存， 比如 登录
        caps['noReset'] = 'true'
        # 不停止APP， 直接执行用例
        caps['dontStopAppOnReset'] = 'true'
        caps['skipDeviceInitialization'] = 'true'
        caps['skipServerInstallation'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_demo(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@resource-id = "com.xueqiu.android:id/post_status"]').click()
        print('by=%s , element=%s' % (By.XPATH, '//*[@resource-id = "com.xueqiu.android:id/post_status"]'))
        self.driver.find_element(By.XPATH, '//*[@resource-id = "com.xueqiu.android:id/iv_close"]').click()
        self.driver.find_element(By.XPATH, '//*[@resource-id = "android:id/tabs"]//*[@text="行情"]').click()
        self.driver.find_element(By.XPATH, '//*[@resource-id = "com.xueqiu.android:id/action_search"]').click()
        self.driver.find_element(By.XPATH, '//*[@resource-id = "com.xueqiu.android:id/search_input_text"]').send_keys(
            "alibaba")
