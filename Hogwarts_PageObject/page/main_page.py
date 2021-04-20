from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from Hogwarts_PageObject.page.add_department import TestAddDepar
from Hogwarts_PageObject.page.add_member import AddMemberPage
from Hogwarts_PageObject.page.base_page import BasePage


class MainPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """
    __ele_contact=(By.ID, "menu_contacts")
    __ele_maingoto=(By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    __ele_addemp=(By.LINK_TEXT, "添加成员")

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(*self.__ele_contact).click()
        return AddMemberPage(self.driver)

    def goto_contact_daper(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(*self.__ele_contact).click()
        return TestAddDepar(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 返回要跳转页面的实例对象
        self.find(*self.__ele_maingoto).click()
        return AddMemberPage(self.driver)

    def comtact_to_add_member(self):
        return AddMemberPage(self.driver)