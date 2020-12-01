from mitmproxy import http
import json


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 将响应数据转换成Python对象，保存到data中
        data = json.loads(flow.response.content)
        # 第一支股票保持原样
        # 第二支股票名字加长一倍
        data['data']['items'][1]['quote']['name'] *= 2
        # 第三支股票名字为空
        data['data']['items'][2]['quote']['name'] = ''
        # 将data的数值类型从字典转换成字符串并赋值给response原始数据格式
        flow.response.text = json.dumps(data)
