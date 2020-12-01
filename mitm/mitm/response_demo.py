from mitmproxy import http


def response(flow: http.HTTPFlow):
    flow.response.headers["count"]
