import pytest
from faker import Faker

from weixin_api.api.externalcontact.tag_api import Tag


def pytest_collection_modifyitems(items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')