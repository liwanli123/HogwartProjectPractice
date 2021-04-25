"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:14 下午'
"""
# app.py  app相关的操作，启动，关闭，重启
from appium import webdriver
from Hogwarts_appium_2.page.base_page import BasePage
from Hogwarts_appium_2.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            print("driver为None，初始化 driver")
            self.log.info("driver为None")
            # 启动app
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["settings[waitForIdleTimeout]"] = 0
            # caps['dontStopAppOnReset'] = True
            caps["noReset"] = "true"
            caps['skipDeviceInitialization'] = True
            # 客户端与服务端建立连接的代码
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待,更智能，中间任何时间等到某个元素都停止查找，继续往后执行，
            # 每次调用find_element的时候都会激活这种等待方式
            self.driver.implicitly_wait(5)
            self.log.info(f"初始化 driver :{self.driver}")
        else:
            # 复用driver
            print("复用 driver")
            self.log.info(f"复用 driver:{self.driver}")
            # start_activity 启动页面，可以运行过程中启动其它app或者当前app的其它页面
            # self.driver.start_activity(package_name, activityname)
            self.driver.launch_app()
        return self

    def restart(self):
        self.log.info("执行重启APP")
        # close_app() 关闭应用
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # quit() 销毁这个driver
        self.log.info(f"销毁driver:{self.driver}")
        self.driver.quit()

    def goto_main(self):
        # 入口
        return MainPage(self.driver)
