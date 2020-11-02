from app.Page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        result = self.main.goto_address().click_addnumber().add_member_menual().add_contact()
        assert result
