from web.podemo2.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "ae"
        account = "aae"
        phonenum = "13546897817"
        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        member = addmember.get_member()
        print(member)
        # assert username in addmember.get_member()
