# request 方法名不能修改
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 增加请求的头信息
    flow.request.headers["myheader"] = "zhu"
    print(flow.request.headers)
