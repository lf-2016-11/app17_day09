import pytest, sys, os

sys.path.append(os.getcwd())  # 添加自定义路径到python搜索路径
from Base.getDriver import get_android_driver
from Base.page import Page


# @pytest.fixture(params=['hello', 'python', 'appium'])
# def data(request):
#     return request.param


class TestSendMessage:
    def setup_class(self):
        # 声明driver对象
        self.driver = get_android_driver("com.android.mms", ".ui.ConversationList")
        # 实例化统一入口
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        # 退出driver
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_add(self, phone=13789897763):
        # 点击新建短信
        self.page_obj.get_add_page().click_add_btn()
        # 输入手机号
        self.page_obj.get_recriver().send_recriver_btn(phone)

    @pytest.mark.parametrize("text", ["appium", "hello", "selenium"])
    def test_message(self, text):
        # 发送短信测试方法
        self.page_obj.get_recriver().send_text(text)
        # 断言
        assert text in self.page_obj.get_recriver().get_text_list()
