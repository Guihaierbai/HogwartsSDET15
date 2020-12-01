from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开保存在本地的数据文件
        with open("D:\\quote.json", encoding="UTF-8") as f:
            # 创建一个response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),
                # 指定返回数据的类型
                {"Content-Type": "application/json"}
            )
