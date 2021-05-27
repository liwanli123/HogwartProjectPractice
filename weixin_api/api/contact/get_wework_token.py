from weixin_api.base.apipage import APIPage


class WeworkToken(APIPage):
    def __init__(self):
        self.token: str = self.get_token()

    def get_token(self):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method': 'get',
            "params": {
                "corpid": "ww0cc5a4a5ed2ea9d7",
                "corpsecret": "wJaKI2SfMWRV6iLd5hGILRNOsdX5jBl7ErPCj6uhMgM"
            }
        }
        r = self.request(data)

        assert r.status_code == 200
        self.token = r.json()['access_token']
        return self.token