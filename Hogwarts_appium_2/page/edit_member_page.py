"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:20 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from Hogwarts_appium_2.page.base_page import BasePage


class EditMemberPage(BasePage):
    __import_Name = (MobileBy.XPATH,
                     "//*[contains(@text,'姓名')]/../"
                     "android.widget.EditText")
    __import_Phonenum =(MobileBy.XPATH,
                  "//*[contains(@text,'手机')]/..//"
                  "android.widget.EditText")
    __find_define =(MobileBy.XPATH, "//*[@text='确定']")

    def edit_member(self, name, phonenum):
        self.log.info(f'保存用户：{name,phonenum}')
        # input name
        # input phonenum
        # click 保存
        self.find(*self.__import_Name).send_keys(name)
        self.find(*self.__import_Phonenum).send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from Hogwarts_appium_2.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def edit_member_again(self, name, phonenum):
        self.log.info(f'保存用户：{name, phonenum}')
        # input name
        # input phonenum
        # click 保存
        self.find(*self.__import_Name).send_keys(name)
        self.find(*self.__import_Phonenum).send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存并继续添加']").click()
        from Hogwarts_appium_2.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def edit_member_delete(self):
        self.log.info('执行删除操作')
        self.swipe_find('删除成员').click()
        self.find(*self.__find_define).click()
        from Hogwarts_appium_2.page.contactlist_page import ContactListPage
        return ContactListPage(self.driver)
