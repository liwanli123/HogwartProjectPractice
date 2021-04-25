from appium.webdriver.common.mobileby import MobileBy
from Hogwarts_appium_2.page.base_page import BasePage


class MemberSettingPage(BasePage):
    __find_Setting = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//"
                                      "android.widget.RelativeLayout/android.widget.TextView")
    __find__EditMember = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def member_setting(self):
        # click 手动输入添加
        self.find(*self.__find_Setting).click()
        self.find(*self.__find__EditMember).click()

        from Hogwarts_appium_2.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)
