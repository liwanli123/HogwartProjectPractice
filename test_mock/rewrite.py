import json
import mitmproxy.http


class Rewrite:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            base_data = json.loads(flow.response.text)
            base_data["data"]["items"][0]["quote"]["name"] = "阿里巴巴101000"
            base_data["data"]["items"][1]["quote"]["name"] = "三三三轻工"

            base_data["data"]["items"][0]["quote"]["percent"] = "0.01"
            base_data["data"]["items"][1]["quote"]["percent"] = "-0.01"
            base_data["data"]["items"][2]["quote"]["percent"] = "0"
            base_data["data"]["items"][3]["quote"]["percent"] = "9999999999999"

            base_data["data"]["items"][0]["quote"]["current"] = '0'
            base_data["data"]["items"][1]["quote"]["current"] = '0.00000001'
            base_data["data"]["items"][2]["quote"]["current"] = '9999999999'
            base_data["data"]["items"][4]["quote"]["current"] = '-1000'
            flow.response.text = json.dumps(base_data)


addons = [
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', '-s', __file__])