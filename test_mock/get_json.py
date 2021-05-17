# coding= utf-8
import json
import mitmproxy.http


# 存在中文乱码情况
class GetJson:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            # 数据的模拟
            data = json.loads(flow.response.text)
            with open("./data/quote.json", "w", encoding="UTF-8") as f:
                json.dump(data, f,indent=2,ensure_ascii=False)
            print("加载入文件完成...")


addons = [
    GetJson()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', "-s", __file__])
