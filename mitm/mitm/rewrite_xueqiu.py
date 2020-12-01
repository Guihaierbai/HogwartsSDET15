from mitmproxy import http
import json


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 将响应数据转换成Python对象，保存到data中
        data = json.loads(flow.response.content)
        # 修改第一支股票的名称
        data['data']['items'][0]['quote']['name'] = "hogwarts1111111"
        # 将data的数值类型从字典转换成字符串并赋值给response原始数据格式
        flow.response.text = json.dumps(data)
