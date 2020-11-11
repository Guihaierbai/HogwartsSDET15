from time import sleep

from frame.xueqiu_blacklist.page.app import App


class TestBlackList:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_blacklist(self):
        self.main.goto_market().goto_search().search()
        sleep(2)
