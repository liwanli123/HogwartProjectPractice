import time
from selenium.webdriver.common.by import By
from Hogwarts_PageObject.page.add_department import TestAddDepar
from Hogwarts_PageObject.page.base_page import BasePage
from Hogwarts_PageObject.page.contact import ContactPage


class AddMemberPage(BasePage):
    # 设定为元祖
    # 页面元素不需要让 业务用例了解，所以要加私有
    __ele_username = (By.ID, "username")
    __ele_accid = (By.ID, "memberAdd_acctid")
    __ele_phone = (By.ID, "memberAdd_phone")
    __ele_save = (By.CSS_SELECTOR, ".js_btn_save")
    __ele_continue = (By.CSS_SELECTOR, ".js_btn_continue")
    __ele_text = (By.LINK_TEXT, "添加成员")
    __ele_contacts = (By.ID, "menu_contacts")

    def add_member(self, username, accid, phone):
        # * 的作用是 解元祖 self.driver.find_element(*username) 等同于
        # self.driver.find_element(By.ID, "username")

        # self.driver.find_element(*self.__ele_username).send_keys(username)
        time.sleep(3)
        self.find(*self.__ele_username).send_keys(username)
        self.find(*self.__ele_accid).send_keys(accid)
        self.find(*self.__ele_phone).send_keys(phone)
        self.find(*self.__ele_save).click()
        # 页面的return 分成两个部分
        # 1. 其他页面的 实例
        # 2. 用例所需要的断言
        # 注意： 不要写成 ContactPage
        # 快捷导入  alt + 回车
        return ContactPage(self.driver)

    def add_member_fail(self,username, accid, phone):
        time.sleep(3)
        self.find(*self.__ele_text).click()
        time.sleep(3)
        self.find(*self.__ele_username).send_keys(username)
        self.find(*self.__ele_accid).send_keys(accid)
        self.find(*self.__ele_phone).send_keys(phone)
        self.find(*self.__ele_save).click()
        element = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        return error_list

    def add_member_continue(self, username, accid, phone):
        # * 的作用是 解元祖 self.driver.find_element(*username) 等同于
        # self.driver.find_element(By.ID, "username")

        # self.driver.find_element(*self.__ele_username).send_keys(username)
        self.find(*self.__ele_username).clear()
        self.find(*self.__ele_accid).clear()
        self.find(*self.__ele_phone).clear()
        time.sleep(1)
        self.find(*self.__ele_username).send_keys(username)
        self.find(*self.__ele_accid).send_keys(accid)
        self.find(*self.__ele_phone).send_keys(phone)
        self.find(*self.__ele_continue).click()
        # 页面的return 分成两个部分
        # 1. 其他页面的 实例
        # 2. 用例所需要的断言
        # 注意： 不要写成 ContactPage
        # 快捷导入  alt + 回车
        return ContactPage(self.driver)

