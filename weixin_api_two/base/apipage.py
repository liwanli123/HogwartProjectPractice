import json
import os
from datetime import datetime
import requests
from loguru import logger

class APIPage:

    def __init__(self):
        self.log = logger
        nowtime = datetime.now()
        time = nowtime.strftime('%Y-%m-%d')
        log_path = os.path.join("../", "log", f"{time}_log.log")
        self.log.remove(handler_id=None)  # 不在控制台输出日志信息
        self.log.add(log_path, retention='30 days', rotation="500 MB", encoding="utf-8", enqueue=True)

    def request(self, request: dict):
        # 为了多协议支持，或者将来协议变更，或者将来方便切换不同的http库，比如requests切换到其他的lib
        if "url" in request:
            self.log.info('使用Http协议测试')
            return self.http_request(request)

        # 创建HTTP请求
    def http_request(self, request):
        r = requests.request(**request)
        self.log.info(f"接口请求数据：{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r

    def rpc_request(self):
        pass

    def tcp_request(self):
        pass
