"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:20 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from Hogwarts_appium_2.page.base_page import BasePage


class AddMemberPage(BasePage):
    __find_AddManually=(MobileBy.XPATH, "//*[@text='手动输入添加']")
    __find_AddedSuccessfully = (MobileBy.XPATH, "//*[@text='添加成功']")

    def addmember_bymenual(self):
        self.log.info("手动输入添加")
        # click 手动输入添加
        self.find(*self.__find_AddManually).click()

        from Hogwarts_appium_2.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.log.info("添加成功")
        self.find(*self.__find_AddedSuccessfully)
        # return True
