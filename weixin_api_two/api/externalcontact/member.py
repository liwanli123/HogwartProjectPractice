import json

import loguru
import pystache as pystache
from weixin_api_two.api.contact.get_wework_token import WeworkToken
from weixin_api_two.uitls.get_data import GetData


class Member(WeworkToken):

    def __init__(self):
        self.log= loguru.logger
        self.baseurl=GetData()
        self.memberurl=self.baseurl.get_UrlData('url','member')
        self.departmenturl=self.baseurl.get_UrlData('url','department')
        self.addurl=self.baseurl.get_UrlData('action','member','create')
        self.searchurl=self.baseurl.get_UrlData('action','member','search')
        self.deleteurl=self.baseurl.get_UrlData('action','member','delete')
        self.deletelisturl = self.baseurl.get_UrlData('action', 'member', 'deletelist')
        self.search_url = self.baseurl.get_UrlData('action', 'department', 'search')

    def search(self):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
            "url": self.memberurl+self.searchurl,
            "method": "get",
            "params": {"access_token": self.token,"department_id": 1,'fetch_child':'1'},
            "json": {}
        }
        return self.request(data)

    def search_department(self):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "url": self.departmenturl + self.search_url,
            "method": "get",
            "params": {"access_token": self.token},
            "json": {}
        }
        return self.request(data)

    def create(self, template: dict):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "url": self.memberurl + self.addurl,
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "userid": "{{userid}}",
                "name": "{{name}}",
                "mobile": "{{mobile}}",
                "department": [1],
                "email": "{{email}}"
            }
        }
        r = self.request(json.loads(pystache.render(json.dumps(data), template)))
        print(r.json())
        return r


    def delete(self, userid):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "url": self.memberurl + self.deleteurl,
            "method": "post",
            "params": {"access_token": self.token,'userid': userid},
            "json": {}
        }
        return self.request(data)

    def delete_list(self, userlist:list):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete",
            "url": self.memberurl + self.deletelisturl,
            "method": "post",
            "params": {"access_token": self.token},
            "json": {"useridlist": userlist }

        }
        return self.request(data)

    def clear(self):
        r = self.search()
        userid=[ id['userid'] for id in r.json()['userlist'] ]
        index=userid.index(GetData().get_ApiData('Administrator')[0])
        userid.pop(index)
        r = self.delete_list(userid)
        return r