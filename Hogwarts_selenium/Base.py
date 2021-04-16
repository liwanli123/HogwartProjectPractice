from time import sleep
import yaml
from selenium import webdriver


class Base:

    def setup(self):
        print("开始执行")
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("data/data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)

    def teardown(self):
        self.driver.quit()
        print("执行结束")