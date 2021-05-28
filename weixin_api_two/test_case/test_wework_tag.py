import allure
from weixin_api_two.api.externalcontact.tag_api import Tag
from weixin_api_two.uitls.contact_info import ContactInfo
from weixin_api_two.uitls.get_data import GetData


class TestWeWorkTag:

    def setup_class(self):
        self.data= GetData()
        self.tag = Tag()
        self.tag.get_token(self.data.get_ApiData('Tagsecret'))
        self.tag.clear()

    def setup(self):
        self.tagdata = ContactInfo().get_text()

    @allure.story("获取标签")
    def test_search(self):
        with allure.step("获取数据"):
            r = self.tag.search()
            allure.attach(f"预期结果为：200，实际结果为：{r.status_code}", attachment_type=allure.attachment_type.TEXT)
            assert r.status_code == 200

        with allure.step("响应状态进行断言"):
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()["errcode"] == 0

    @allure.story("添加标签")
    def test_tag(self):
        with allure.step("添加数据"):
            r = self.tag.add(self.tagdata, self.tagdata)
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()["errcode"] == 0

        with allure.step("获取列表数据进行断言"):
            r = self.tag.search()
            tag_id_list = [tag['name'] for group in r.json()['tag_group'] for tag in group['tag']]
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()["errcode"] == 0

            allure.attach(f"预期结果为：{self.tagdata}，实际结果为：{self.tagdata in tag_id_list}",
                          name="预期结果在实际结果中",
                          attachment_type=allure.attachment_type.TEXT)
            assert self.tagdata in tag_id_list

    @allure.story("删除标签")
    def test_delete(self):
        with allure.step("添加删除数据"):
            r = self.tag.search()
            delete_list=[self.tag.add(self.tagdata, self.tagdata).json()["tag_group"]["group_id"]]
        # delete_list = [group['group_id'] for group in self.tag.search().json()["tag_group"]]

        with allure.step("删除数据"):
            r = self.tag.delete(group_id=delete_list)

            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()["errcode"] == 0

        with allure.step("获取列表数据"):
            r = self.tag.search()
            tag_id_list = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag']]
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()["errcode"] == 0

            allure.attach(f"预期结果为：{delete_list}，实际结果为：{delete_list not in tag_id_list}",
                          name="预期结果不在实际结果中",
                          attachment_type=allure.attachment_type.TEXT)
            assert delete_list not in tag_id_list
