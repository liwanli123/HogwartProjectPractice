import os

import yaml
from selenium import webdriver


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver 的实例化
    """
    # 没有参数传入， 会取默认None ,如果有参数传入,会取传入的参数
    def __init__(self, base_driver=None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param base_driver:
        """
        self.wexi_cookies()
        if base_driver == None:
            self.driver = webdriver.Chrome()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("../data/data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，每一次调用find 方法，就会轮询查找元素是否存在
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele = None):
        """
        :param by: 定位方式 css, xpath, id
        :param ele: 元素定位信息
        :return:
        """
        # 两种传入定位元素的方式，提高代码的兼容性
        # 如果传入的是元祖,那就只有一个参数
        if ele == None:
            # 比如传入(By.ID, "username")
            # * 的作用是 解元祖 self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID, "username")
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def wexi_cookies(self):
        if os.path.isfile("../data/data.yaml"):
            pass
        else:
            # 复用只支持chrome浏览器
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            # 获取cookie信息
            cookie = self.driver.get_cookies()
            # 把cookie存如yaml文件内
            with open("../data/data.yaml", "w", encoding="UTF-8") as f:
                yaml.dump(cookie, f)