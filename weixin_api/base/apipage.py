import json
import requests


class APIPage:
    def request(self, request: dict):
        # 为了多协议支持，或者将来协议变更，或者将来方便切换不同的http库，比如requests切换到其他的lib
        if "url" in request:
            return self.http_request(request)

        # 创建HTTP请求
    def http_request(self, request):
        r = requests.request(**request)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self):
        pass

    def tcp_request(self):
        pass
