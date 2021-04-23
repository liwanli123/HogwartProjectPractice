from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestWeichatClock:
    def setup(self):
        # 初始化
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"]=''
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["settings[waitForIdleTimeout]"] = 100
        caps["noReset"] = "true"
        # caps['skipServerInstallation'] = 'true'
        # caps['skipDeviceInitialization'] = 'true'
        # caps['dontStopAppOnReset'] = 'true'
        caps['settings[waitForIdleTimeout]'] = 200  # 等待页面空闲的时间
        # 客户端与服务端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待,更智能，中间任何时间等到某个元素都停止查找，继续往后执行，
        # 每次调用find_element的时候都会激活这种等待方式
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源消毁
        self.driver.quit()


    def test_clock_in(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guo").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ap6").click()
        ele=self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/mr")
        assert_that(ele.text,contains_string('外出打卡成功'))