"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:18 下午'
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from Hogwarts_appium_2.page.add_member_page import AddMemberPage
from Hogwarts_appium_2.page.base_page import BasePage
from Hogwarts_appium_2.page.member_setting_page import MemberSettingPage


class ContactListPage(BasePage):
    __find_getNameList=(MobileBy.XPATH,"//*[@text='添加成员']/../../../../../..//android.widget.TextView")

    def goto_addmember(self):
        self.log.info('寻找添加成员按钮')
        # click 添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_deletemember(self,name):
        self.log.info(f'选择删除用户：{name}')
        self.swipe_find(name).click()
        return MemberSettingPage(self.driver)

    def get_list(self):
        sleep(4)
        data_list = self.finds(*self.__find_getNameList)
        name_list= []
        for ele in data_list:
            if ele.text=='我的客户':
                pass
            elif ele.text=='企业通讯录':
                pass
            elif ele.text=='添加成员':
                pass
            elif "共" in ele.text:
                pass
            else:
                name_list.append(ele.text)

        self.log.info(f'get_list返回列表为：{name_list}')
        return name_list
