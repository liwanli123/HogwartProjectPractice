"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 4:48 下午'
"""

# base_page.py 基类，init，
# 封装一些最基本的方法，便于后续维护
import os
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from loguru import logger


class BasePage:
    def __init__(self, driver: WebDriver = None):
        # 初始化driver
        self.driver = driver
        self.log = logger
        nowtime=time.strftime('%Y-%m-%d')
        log_path = os.path.join("../", "log", f"{nowtime}_log.log")
        self.log.remove(handler_id=None)  # 不在控制台输出日志信息
        self.log.add(log_path, retention='30 days', rotation="500 MB", encoding="utf-8", enqueue=True)

    def find(self, by, value):
        self.log.info(f"定位方式为{by}")
        self.log.info(f"定位元素为{value}")
        # 查找元素
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        self.log.info(f"定位方式为{by}")
        self.log.info(f"定位元素为{value}")
        # 查找元素
        return self.driver.find_elements(by, value)

    def swipe_find(self, text, num=5):
        # num : 默认查找次数
        # 进入滑动查找，改变隐式等待时长，提高查找速度
        self.driver.implicitly_wait(1)

        # 滑动查找，通过外部传递的num次数，决定查找次数
        for i in range(num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                self.log.info("未找到，滑动")
                print("未找到，滑动")
                # 滑动一页，继续查找
                size = self.driver.get_window_size()
                # self.driver.get_window_rect()
                width = size['width']
                height = size['height']
                # 'width', 'height'
                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                duration = 2000  # ms
                # 完成滑动操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num:
                # 如果达到 num-1次没有找到，则抛出这个异常
                self.driver.implicitly_wait(5)
                self.log.info(f"找了{i}次，未找到")
                raise NoSuchElementException(f"找了{i}次，未找到")
