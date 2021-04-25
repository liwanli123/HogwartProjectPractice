import pytest
from Hogwarts_appium_2.page.app import App
from Hogwarts_appium_2.utils.contact_info import ContactInfo
from Hogwarts_appium_2.utils.getdata import get_contact


class TestContactAgain:
    def setup_class(self):
        self.contactinfo = ContactInfo()
        self.app = App()
        self.main = self.app.start().goto_main().\
            goto_contactlist(). \
            goto_addmember().addmember_bymenual()

    def setup(self):
        # 启动 app
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        self.app.stop()


    @pytest.mark.parametrize("name,phone",get_contact())
    def test_add_again_contact(self,name,phone):
        self.main.edit_member_again(name, phone).find_toast()

