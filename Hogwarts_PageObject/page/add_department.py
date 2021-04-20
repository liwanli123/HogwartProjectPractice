from time import sleep

from selenium.webdriver.common.by import By
from Hogwarts_PageObject.page.base_page import BasePage
from Hogwarts_PageObject.page.contact import ContactPage


class TestAddDepar(BasePage):

    __ele_adddapar=(By.CSS_SELECTOR,".js_add_sub_party")
    __ele_input=(By.CSS_SELECTOR, ".inputDlg_item>input")
    __ele_cancel=(By.CSS_SELECTOR, "[d_ck='cancel']")
    __ele_submit=(By.CSS_SELECTOR,"[d_ck='submit']")
    __ele_tips=(By.ID, "js_tips")

    def add_department(self,name):
        self.find(*self.__ele_adddapar).click()
        self.find(*self.__ele_input).send_keys(name)
        self.find(*self.__ele_submit).click()
        return ContactPage(self.driver)

    def exit_department(self,name):
        sleep(1)
        self.find(*self.__ele_adddapar).click()
        self.find(*self.__ele_input).send_keys(name)
        self.find(*self.__ele_cancel).click()
        return ContactPage(self.driver)

    def add_department_false(self,name):
        self.find(*self.__ele_adddapar).click()
        self.find(*self.__ele_input).send_keys(name)
        self.find(*self.__ele_submit).click()
        element =self.find(*self.__ele_tips)
        sleep(2)
        if element.text=="请输入部门名称":
            self.find(*self.__ele_cancel).click()
        print(element.text)
        sleep(2)
        return ContactPage(self.driver)