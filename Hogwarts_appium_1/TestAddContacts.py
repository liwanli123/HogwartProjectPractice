from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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


    def test_save(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hfj").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys("贺岁档")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys("15900000230")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac9").click()
        assert self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

    def test_add_save(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hfj").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys("贺岁图")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys("15900001230")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac_").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys("胡不用")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys("15905001230")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ac_").click()
        assert self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

