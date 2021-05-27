from weixin_api.api.contact.get_wework_token import WeworkToken

class Tag(WeworkToken):

    def search(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {}
        }
        return self.request(data)

    def add(self, tag_list, group_name):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
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
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "method": "post",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id,
                "tag_id": tag_id
            }
        }
        return self.request(data)

    def clear(self):
        r = self.search()
        tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
        r = self.delete(tag_id_list)
        return r