from Base.base import Base
from Page.pageElements import PageElements


class RecriverPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 点击短信发送页面信息
    def send_recriver_btn(self, phone):
        #输入手机号
        self.send_ele(PageElements.recriver_btn_xpath, phone)

    def send_text(self, text):
        #输入内容
        self.send_ele(PageElements.add_text_btn_xpath, text)
        #点击发送
        self.click_ele(PageElements.click_on_btn_id)

    def get_text_list(self):
         # 定位所有内容
        results = self.search_eles(PageElements.text_ids)
         #返回文本列表
        return [i.text for i in results]
