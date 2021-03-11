import json

import requests


class Tag:
    # 获取token
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': 'ww0108b0936456c314', 'corpsecret': 'bMC77iBoxIs3Fnlt7XYuKQNsYX-8Ma9bpRBmwp1mfkE'}
        )
        token = r.json()['access_token']
        return token

    def get_list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={
                'access_token': self.get_token()},
            json={
                "group_id": []
                # "tag_id": []
            }
        )
        return r

    def add(self, group_name, tag_name, **kwargs):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={
                'access_token': self.get_token()},
            json={
                "group_name": group_name,
                "tag": tag_name,
                **kwargs
            }
        )
        return r

    def update(self, id, new_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={
                'access_token': self.get_token()},
            json={
                "id": id,
                "name": new_name
            })
        return r

    def delete_group(self, group_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={
                'access_token': self.get_token()},
            json={
                'group_id': group_id
            }
        )
        return r

    def delete_tag(self, tag_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={
                'access_token': self.get_token()},
            json={
                'tag_id': tag_id
            }
        )
        return r
