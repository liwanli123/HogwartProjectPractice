import os
from time import sleep
import pytest
import yaml
from selenium import webdriver
from Hogwarts_selenium.Base import Base


class Test_Wework(Base):

    # 复用浏览器
    @pytest.fixture(scope="function")
    def wework_cookies(self):
        if os.path.isfile("data/data.yaml"):
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
            with open("data/data.yaml", "w", encoding="UTF-8") as f:
                yaml.dump(cookie, f)

    @pytest.mark.usefixtures("wework_cookies")
    def test_save_and_continue_adding(self):
        # 在当前页面点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
        # 使用文本搜索
        self.driver.find_element_by_link_text("添加成员").click()
        sleep(3)
        # 填写数据
        self.driver.find_element_by_id("username").send_keys('张大舅')
        self.driver.find_element_by_id("memberAdd_english_name").send_keys('男')
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(123459)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(15936585235)
        self.driver.find_element_by_id("memberAdd_title").send_keys("普通员工")
        sleep(1)
        self.driver.find_element_by_link_text("保存并继续添加").click()
        sleep(3)
        self.driver.find_element_by_id("username").send_keys('刻大舅')
        self.driver.find_element_by_id("memberAdd_english_name").send_keys('男')
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(123959)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(15536585235)
        self.driver.find_element_by_id("memberAdd_title").send_keys("普通员工")
        sleep(1)
        self.driver.find_element_by_link_text("保存并继续添加").click()
        sleep(3)
        self.driver.find_element_by_id("1688850938153040_anchor")
        sleep(3)

    # 使用序列化cookie的方法登录
    @pytest.mark.usefixtures("wework_cookies")
    def test_save(self):
        # 在当前页面点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
        # 使用文本搜索
        self.driver.find_element_by_link_text("添加成员").click()
        sleep(3)
        self.driver.find_element_by_id("username").send_keys('里大舅')
        self.driver.find_element_by_id("memberAdd_english_name").send_keys('男')
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(123456)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(15936585236)
        self.driver.find_element_by_id("memberAdd_title").send_keys("普通员工")
        sleep(1)
        self.driver.find_element_by_link_text("保存").click()
        sleep(3)
