#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        # get_cookies() 可以获取当前打开页面的cookies信息
        # add_cookies() 可以将cookies信息添加到当前打开的页面
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '7-GSqJwuvAnULIJWYbEjvQ4Ab_FA52UXxRdgm5G0IZmXPw4lQQKuk7OGkDldyP-gBZCQoo_CVK25RzqOtaHlVWr03cesXwndzDvJ4dnsis16vCgVnUiao5bjajUNLtyVh2iqLXv3COVOZN3vT56vBkqKDg84SDkWTdyrsYk3_Gwk0EiooUmV3wcdya2ieSo-E9yYWhLfdFJKFaTBBowNrZAcz58D2jCuGGF6YiFglkrKI5E3nQNtcjUY4EsCLgGThG8GwlfRvgnP2fsOlSlhPQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851921250426'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634890599, 'httpOnly': False,
                                            'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                            'secure': True, 'value': '1603354466'},
            {'domain': '.qq.com', 'expiry': 1603459524, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.744575675.1603372512'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603386000, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3ih62r4'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'fHmhj5huhThvuWqyM5TNn8B7xOu-KXjsvtYKLTSWestO9QI77nyPwSEAtxz-aiN0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634890464, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1914890767, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '1_769456011'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851921250426'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1603386000, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '3ih62r4'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': True, 'value': '769456011'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '22815482122970383'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '9783778175'},
            {'domain': '.qq.com', 'expiry': 1666445124, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1977516214.1603372512'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '77601a00064525e8f2062ac139560efaf64009fb90eaf6b3f3c4a2cdffea8377'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1914800891, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': '55ab945dda1ebe75'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4200038'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'CEyBbrcDTD'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1605967409, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325049167295'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '1525084160'}]
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        db['cookie'] = cookies
        cookies = db['cookie']
        db.close()

        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        time.sleep(3)
        # 定位"导入通讯录"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        time.sleep(3)
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            "D:\\data.xlsx")
        # 验证上传的文件名
        file_name = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "data.xlsx" == file_name
        sleep(3)
