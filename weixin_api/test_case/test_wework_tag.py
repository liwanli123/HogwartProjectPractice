from weixin_api.api.externalcontact.tag_api import Tag


class TestWeWorkTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.clear()

    def test_search(self):
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag(self):
        # 新增标签
        # todo: 数据唯一性，1.提前清理数据（推荐） 2.使用时间戳代表唯一性
        r = self.tag.add("tag_052001", "tag_group_052001")
        assert r.json()['errcode'] == 0

        # todo：代码冗余
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_delete(self):
        r = self.tag.search()
        delete_list=[self.tag.add("GG55", "GG55").json()["tag_group"]["group_id"]]
        # delete_list = [group['group_id'] for group in self.tag.search().json()["tag_group"]]
        r = self.tag.delete(group_id=delete_list)
        assert r.json()['errcode'] == 0

