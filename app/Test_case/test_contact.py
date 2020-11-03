from app.Page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "test006"
        gender = "男"
        phonenum = "13522115450"

        result = self.main.goto_address() \
            .click_addnumber() \
            .add_member_menual() \
            .add_contact(name, gender, phonenum).get_toast()
        # print(result)
        assert '添加成功' == result
