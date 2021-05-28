from weixin_api_two.api.contact.get_wework_token import WeworkToken
from weixin_api_two.uitls.get_data import GetData
import loguru


class Tag(WeworkToken):

    def __init__(self):
        self.baseurl=GetData()
        self.log= loguru.logger
        self.tagurl=self.baseurl.get_UrlData('url','tag')
        self.addurl=self.baseurl.get_UrlData('action','tag','add')
        self.searchurl=self.baseurl.get_UrlData('action','tag','search')
        self.deleteurl=self.baseurl.get_UrlData('action','tag','delete')

    def search(self):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "url": self.tagurl + self.searchurl,
            "method": "post",
            "params": {"access_token": self.token},
            "json": {}
        }
        return self.request(data)

    def add(self, tag_list, group_name):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "url": self.tagurl+self.addurl,
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                        "group_name": group_name,
                        "tag": [{
                                "name": tag_list,
                            }],
                    }
        }
        return self.request(data)

    def delete(self, group_id: list = None, tag_id: list = None):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "url":  self.tagurl + self.deleteurl,
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id,
                "tag_id": tag_id
            }
        }
        return self.request(data)

    def delete_list(self, tag_id_list):
        data = {
            # "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "url": self.tagurl + self.deleteurl,
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id_list
            }
        }
        return self.request(data)

    def clear(self):
        r = self.search()
        tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        r = self.delete_list(tag_id_list)
        return r
