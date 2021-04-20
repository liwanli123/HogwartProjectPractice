import pytest
from Hogwarts_PageObject.page.getdata import get_department, get_employee, get_employee_one as one
from Hogwarts_PageObject.page.main_page import MainPage


class TestAddMember:
    """
    编写测试用例
    """
    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("username, accid, phone", one())
    def test_add_member(self, username, accid, phone):
        # 1. 跳转到添加成员页面  2. 添加成员   3. 获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert username in name_list

    @pytest.mark.parametrize("username, accid, phone",one())
    def test_add_member_fail(self, username, accid, phone):
        data_list = self.main_page.goto_contact().add_member_fail(username, accid, phone)
        err = [i for i in data_list if i != ""]
        assert username in err[0]

    @pytest.mark.parametrize("username, accid, phone",get_employee())
    def test_add_member_contact(self, username, accid, phone):
        data_list = self.main_page.comtact_to_add_member().add_member_continue(username, accid, phone)