import allure
from weixin_api_two.api.externalcontact.member import Member
from weixin_api_two.uitls.contact_info import ContactInfo
from weixin_api_two.uitls.get_data import GetData


class TestWeWorkTag:

    def setup_class(self):
        self.data = GetData()
        self.member = Member()
        self.member.get_token(self.data.get_ApiData('Membersecret'))
        self.member.clear()

    def setup(self):
        self.userid = ContactInfo().get_pystr()
        self.name = ContactInfo().get_name()
        self.mobile = ContactInfo().get_phonenum()
        self.email = ContactInfo().get_email()

    @allure.story("查看部门")
    def test_search_department(self):

        with allure.step("发起请求,获取响应数据"):
            r = self.member.search_department()
            assert r.status_code == 200
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()['errcode'] == 0

    @allure.story("查看成员")
    def test_search(self):

        with allure.step("发起请求,获取响应数据"):
            r = self.member.search()
            assert r.status_code == 200
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()['errcode'] == 0

    @allure.story("创建成员")
    def test_create(self):
        template = {"userid": self.userid, "name": self.name, "mobile": self.mobile, "email": self.email}
        r = self.member.create(template)
        assert r.status_code == 200

        with allure.step("发起请求,获取响应数据"):
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()['errcode'] == 0

        with allure.step("获取列表数据进行断言"):
            datalist = self.member.search()
            assert self.userid in [ id['userid'] for id in datalist.json()['userlist'] ]
            allure.attach(f"预期结果为：{self.userid}，实际结果为：{[ id['userid'] for id in datalist.json()['userlist'] ]}",
                          name="预期结果在实际结果中",attachment_type=allure.attachment_type.TEXT)

    @allure.story("删除成员")
    def test_delete(self):

        with allure.step("发起请求,创建成员"):
            template = {"userid": self.userid, "name": self.name, "mobile": self.mobile, "email": self.email}
            r = self.member.create(template)
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()['errcode'] == 0

        with allure.step("发起请求,获取成员"):
            r = self.member.search()
            userid=[ id['userid'] for id in r.json()['userlist'] ]
            assert self.userid in userid
            allure.attach(f"预期结果为：{self.userid}，实际结果为：{self.userid in userid}",
                          name="预期结果在实际结果中",attachment_type=allure.attachment_type.TEXT)

        index=userid.index(self.data.get_ApiData('Administrator')[0])
        userid.pop(index)

        with allure.step("发起请求,删除成员"):
            r = self.member.delete(userid)
            allure.attach(f"预期结果为：0，实际结果为：{r.json()['errcode']}", attachment_type=allure.attachment_type.TEXT)
            assert r.json()['errcode'] == 0

        with allure.step("获取列表数据进行断言"):
            r = self.member.search()
            useridlist=[ id['userid'] for id in r.json()['userlist'] ]
            assert userid not in useridlist
            allure.attach(f"预期结果为：{self.userid}，实际结果为：{self.userid not in userid}",
                          name="预期结果不在实际结果中",attachment_type=allure.attachment_type.TEXT)
