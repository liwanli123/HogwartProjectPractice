"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:23 下午'
"""
import pytest
from Hogwarts_appium_2.page.app import App
from Hogwarts_appium_2.utils.contact_info import ContactInfo
from Hogwarts_appium_2.utils.getdata import get_contact


class TestContact:
    def setup_class(self):
        self.contactinfo = ContactInfo()
        self.app = App()

    def setup(self):
        # 启动 app
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_add_contact(self):
        name = self.contactinfo.get_name()
        phonenum = self.contactinfo.get_phonenum()

        self.main.goto_contactlist(). \
            goto_addmember().addmember_bymenual(). \
            edit_member(name, phonenum).find_toast()

    def test_delete_member(self):
        name_list=self.main.goto_contactlist().get_list()
        res_list= self.main.goto_contactlist(). \
            goto_deletemember(name_list[1]).member_setting(). \
            edit_member_delete().get_list()

        assert name_list[1] not in res_list


    @pytest.mark.parametrize("name,phone",get_contact())
    def test_delete_members(self,name,phone):
        name_list= self.main.goto_contactlist(). \
            goto_deletemember(name).member_setting(). \
            edit_member_delete().get_list()

        assert name not in name_list


