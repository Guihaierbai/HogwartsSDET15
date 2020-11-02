from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWX():
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        # 保留缓存， 比如 登录
        caps['noReset'] = 'true'
        # 不停止APP， 直接执行用例
        caps['donStopAppOnReset'] = 'true'
        caps['skipDeviceInitialization'] = 'true'
        caps['skipServerInstallation'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_contacts(self):
        '''
        添加联系人
        :return:
        '''
        name = "test003"
        gender = "男"
        phonenum = "13522115457"

        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 设置姓名，性别，手机号
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/../*[@class='android.widget.RelativeLayout']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机') and contains(@class,'TextView')]/..//android.widget.EditText").send_keys(
            phonenum)
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # sleep(2)
        # 打印页面布局，方便定位toast
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        assert result
