import pytest

from Hogwarts_PageObject.page.getdata import get_department, get_otherdepar
from Hogwarts_PageObject.page.main_page import MainPage


class TestDepar:

    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("name",get_department())
    def test_add_department_exit(self,name):
        depar_list=self.main_page.goto_contact_daper().exit_department(name).get_department_list(name)
        print(depar_list)

    @pytest.mark.parametrize("name",get_department())
    def test_add_department(self,name):
        depar_list=self.main_page.goto_contact_daper().add_department(name).get_department_list(name)
        print(depar_list)

    @pytest.mark.parametrize("name",get_otherdepar())
    def test_add_department_false(self,name):
        self.main_page.goto_contact_daper().add_department_false(name)