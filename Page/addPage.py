from Base.base import Base
from Page.pageElements import PageElements


class AddPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)  #driver给base的初始化方法用

    # 点击新增短信页面
    def click_add_btn(self):
        #点击新建短信按钮
        self.click_ele(PageElements.add_message_btn_id)
