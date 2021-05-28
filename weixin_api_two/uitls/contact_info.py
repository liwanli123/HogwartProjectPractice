"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/24 5:10 下午'
"""
from faker import Faker
from loguru import logger

from weixin_api_two.base.apipage import APIPage


class ContactInfo(APIPage):
    def __init__(self):
        self.log = logger
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        self.log.info(f'name数据：{name}')
        return name

    def get_pystr(self):
        pystr=self.faker.pystr()
        self.log.info(f'pystr数据：{pystr}')
        return pystr

    def get_phonenum(self):
        phonenum = self.faker.phone_number()
        self.log.info(f'phonenum 数据：{phonenum}')
        return phonenum

    def get_email(self):
        email = self.faker.email()
        self.log.info(f'email数据：{email}')
        return email

    def get_text(self):
        text = self.faker.address()
        self.log.info(f'tag数据：{text}')
        return text
