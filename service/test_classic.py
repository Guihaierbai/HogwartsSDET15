import datetime
import json
import time

import requests


# done: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# done: 代码冗余，需要封装
# done: 无法清晰的描述业务
# done: 数据结构比较简单时使用jsonpath表达更灵活的递归查找
def test_tag_list():
    corpid = 'ww0a52c5c09df57d37'
    corpsecret = 'pgE6VafDFG1vPK5lXatbQ1Jn5u-j3NVmiW_0vhSyI8g'
    # 获取token
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    token = r.json()['access_token']

    # 获取标签列表
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            "tag_id": []
        }
    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    # 根据tag_id修改对应tag_name
    tag_name = "tag1_new1" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={"access_token": token},
        json={
            "id": "etv82lDAAANkzTMv21Copenpeh5tzUFw",
            "name": tag_name
        }
    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    # 如找到，tags中有tag，如未找到，tags为空
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'Guihaierbai'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    assert tags != []
