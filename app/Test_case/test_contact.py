from selenium.common.exceptions import NoSuchElementException

from app.Page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        # 测试添加成员
        name = "test007"
        gender = "男"
        phonenum = "13522115410"

        result = self.main.goto_address() \
            .click_addnumber() \
            .add_member_menual() \
            .add_contact(name, gender, phonenum).get_toast()
        # print(result)
        assert '添加成功' == result

    def test_deletecontact(self):
        # 测试删除成员
        name = "test007"
        self.main.goto_address().click_number(name).contact_setting().edit_number().delete_contact()
        try:
            self.app.find_by_scroll(name)
        except NoSuchElementException as e:
            print("成员已被删除")
            return False
        else:
            print("成员删除失败")
            return True
