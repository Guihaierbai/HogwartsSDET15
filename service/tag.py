import datetime
import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
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
        return token

    def add(self, group_name, tag, **kwargs):
        # 添加标签
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={"access_token": self.token},
            json={
                "group_name": group_name,
                "tag": tag,
                **kwargs
            }
        )
        print(json.dumps(r.json(), indent=2))

    def list(self):
        # 获取标签列表
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={
                "tag_id": []
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        # 根据tag_id修改对应tag_name
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                "id": id,
                "name": tag_name
            }
        )
        # print(json.dumps(r.json(), indent=2))
        return r

    # 查询tag_id -> 删除
    def delete(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                # "tag_id": ['etv82lDAAA30zOLHzBVqRsJrv2LZABsA'],
                "group_id": ['etv82lDAAATecTA2N-sC9BbqgOEZoXzg']
            }
        )
        print(json.dumps(r.json(), indent=2))
