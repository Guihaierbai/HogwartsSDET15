import datetime
import json

import pytest

from service.tag_2 import Tag


class TestTag:

    def setup(self):
        self.tag = Tag()

    def test_list(self):
        r = self.tag.get_list()
        print("1111111" + json.dumps(r.json(), indent=2))

    @pytest.mark.parametrize('group_name, tag_name',
                             [("group_2", [{"name": "tag_3"}]), ("group_3", [{"name": "tag_4"}])]
                             )
    def test_add(self, group_name, tag_name):
        r = self.tag.add(group_name, tag_name)
        assert r.json()['errcode'] == 0
        assert r.status_code == 200
        # r = self.tag.get_list()
        # print("1111111"+json.dumps(r.json()))

    @pytest.mark.parametrize('id, new_name, group_name',
                             [('etC6ljBgAAnEuSPc6NmmaZdBF8PwJqig', 'wahaha', 'group_2')])
    def test_update(self, id, new_name, group_name):
        new_name = new_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.update(id, new_name)
        r = self.tag.get_list()
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['name'] == new_name
        ]
        # assert jsonpath(r.json(), "$..[?(@.name='{tag_name}')]") is not None
        # print("tags:%s" %tags)
        assert tags != []

    def test_delete_tag(self, ):
        tag_id = 'etC6ljBgAAZzXIaV1a481S2FgLSuKlVg'
        group_name = 'group_2'
        r = self.tag.delete_tag(tag_id)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        r = self.tag.get_list()
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['id'] == tag_id
        ]
        assert tags == []

    def test_delete_group(self):
        r = self.tag.get_list()
        # lista = [item.get('group_id') for item in r.json()['tag_group']]
        # print(lista)
        group_id = []
        for group in r.json()['tag_group']:
            if group:
                group_id.append(group['group_id'])

        for id in group_id:
            r = self.tag.delete_group(id)
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
