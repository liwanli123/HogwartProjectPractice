import mitmproxy.http
from mitmproxy import http


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
        in flow.request.url and "x=" in flow.request.url:
            with open("./data/doquote.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read()
                )


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', "-s", __file__])
