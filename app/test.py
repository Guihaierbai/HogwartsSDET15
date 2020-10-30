import time

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
desired_caps['noReset'] = "true"
desired_caps['dontStopAppOnRest'] = "true"
desired_caps['skipDeviceInitialization'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
time.sleep(2)

driver.quit()
