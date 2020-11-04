'''
添加成员页
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from app.Page.base_page import BasePage


class AddMemberPage(BasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self, username, account, phonenum):
        time.sleep(2)
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        contactlist = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

        print(contactlist)
        titlelist = []
        for element in contactlist:
            titlelist.append(element.get_attribute("title"))

        return titlelist
