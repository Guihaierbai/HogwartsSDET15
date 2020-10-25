from testing.podemo2.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "ab"
        account = "aab"
        phonenum = "13546897814"
        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member()
