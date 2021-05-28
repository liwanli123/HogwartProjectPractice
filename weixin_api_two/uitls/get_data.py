import yaml
from weixin_api_two.base.apipage import APIPage


class GetData(APIPage):

    # 获取配置数据
    def get_ApiData(self, category: str) -> dict or list or str:
        self.log.info("调用了get_ApiData")
        self.log.info(f"使用的是:{category}")
        with open("../datas/generaldata.yaml", encoding="utf-8") as f:
            BaseDatas = yaml.safe_load(f)
        return BaseDatas[category]


    # 获取测试数据
    def get_UrlData(self, url: str, name: str,action: str = None) -> dict or list or str:
        self.log.info("调用了get_UrlData")
        self.log.info(f"获取方式{url}")
        self.log.info(f"测试功能{name}")
        self.log.info(f"测试动作{action}")
        with open("../datas/urldata.yaml", encoding="utf-8") as f:
            TestDatas = yaml.safe_load(f)
        if(action==None):
            return TestDatas[url][name]
        else:
            return TestDatas[url][name][action]

