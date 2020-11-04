'''
企业微信首页
'''
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.Page.base_page import BasePage
from web.podemo2.page.add_member_page import AddMemberPage


class MainPage(BasePage):
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def goto_addmember(self):
        # 封装添加成员方法
        time.sleep(2)
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)
