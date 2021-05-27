import yaml


class GetData:

    # 获取配置数据
    def get_BaseData(self, category: str) -> dict or list or str:
        # logging.info("调用了get_BaseData")
        # logging.info(f"使用的是:{category}")
        with open("../datas/BaseDatas.yml", encoding="utf-8") as f:
            BaseDatas = yaml.safe_load(f)
        return BaseDatas[category]

    # 获取测试数据
    def get_TestData(self, modular: str, function: str) -> dict or list or str:
        # logging.info("调用了get_TestData")
        # logging.info(f"测试模块{modular}")
        # logging.info(f"测试方法{function}")
        with open("../test_datas/TestDatas.yml", encoding="utf-8") as f:
            TestDatas = yaml.safe_load(f)
        return TestDatas[modular][function]