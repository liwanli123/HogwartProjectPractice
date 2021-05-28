from weixin_api_two.base.apipage import APIPage


class WeworkToken(APIPage):

    def get_token(self,secret):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method': 'get',
            "params": {
                "corpid": "ww0cc5a4a5ed2ea9d7",
                "corpsecret": secret
            }
        }
        r = self.request(data)

        assert r.status_code == 200
        self.token = r.json()['access_token']
        self.log.info(f"获取的token:{self.token}")
        return self.token