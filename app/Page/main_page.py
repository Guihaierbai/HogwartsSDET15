'''
首页
'''
from app.Page.addresslist_page import AddressListPage


class MainPage:
    def goto_message(self):
        # 进入消息页
        pass

    def goto_address(self):
        # 进入通讯录页
        return AddressListPage()
