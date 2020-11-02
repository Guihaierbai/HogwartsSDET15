'''
邀请页面
'''
from app.Page.contactadd_page import ContactAddPage


class MemberInviteMenuPage:
    def add_member_menual(self):
        # 点击手动输入添加
        return ContactAddPage()
