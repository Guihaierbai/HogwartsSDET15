import datetime
import json
import time

import pytest
import requests

# done: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# done: 代码冗余，需要封装
# done: 无法清晰的描述业务
# done: 数据结构比较简单时使用jsonpath表达更灵活的递归查找
from jsonpath import jsonpath

from service.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    # 更新标签
    @pytest.mark.parametrize("tag_id, tag_name, group_name", [
        ["etv82lDAAANkzTMv21Copenpeh5tzUFw", "tag1_new_", "Guihaierbai"],
        ["etv82lDAAANkzTMv21Copenpeh5tzUFw", "tag1_new_中文", "Guihaierbai"],
        ["etv82lDAAANkzTMv21Copenpeh5tzUFw", "tag1_new_!@#", "Guihaierbai"]
    ])
    def test_tag_update(self, tag_id, tag_name, group_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        # print(json.dumps(r.json(), indent=2))
        # print("group_name:%s" %group_name)
        # 如找到，tags中有tag，如未找到，tags为空
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        # assert jsonpath(r.json(), "$..[?(@.name='{tag_name}')]") is not None
        # print("tags:%s" %tags)
        assert tags != []

    def test_add_tag(self):
        # todo： 测试数据要放到数据文件中
        group_name = "group1"
        tag = [
            {"name": "tag1"},
            {"name": "tag2"},
            {"name": "tag3"}
        ]
        self.tag.add(group_name, tag)

    def test_list(self):
        # groupid etv82lDAAATecTA2N-sC9BbqgOEZoXzg
        # tag1 id etv82lDAAA30zOLHzBVqRsJrv2LZABsA
        self.tag.list()

    # 40068 非法的tagid
    # 1. 删除接口有问题
    # 2. 再进行重试（重试次数：N）： 手动实现或借助pytest钩子（rerun插件）
    #    a. 在添加一个接口
    #    b. 对添加的接口再删除
    #    c. 查询是否删除成功
    def test_delete_tag(self):
        self.tag.delete()
