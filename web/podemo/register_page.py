from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 注册信息
    def register_success(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("aaaa")
        self.driver.find_element(By.ID, "manager_name").send_keys("ada")
        self.driver.find_element(By.ID, "register_tel").send_keys("12313")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
