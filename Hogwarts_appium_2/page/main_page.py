"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:16 下午'
"""

# 主页面
from appium.webdriver.common.mobileby import MobileBy
from Hogwarts_appium_2.page.base_page import BasePage
from Hogwarts_appium_2.page.contactlist_page import ContactListPage


class MainPage(BasePage):
    __contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        # click 通讯录
        self.find(*self.__contact_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactListPage(self.driver)
