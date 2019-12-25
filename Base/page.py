#统一入口类
from Page.addPage import AddPage
from Page.recriverPage import RecriverPage


class Page:
    def __init__(self,driver):
        self.driver=driver

    #返回新增页面实例化对象
    def get_add_page(self):
        return AddPage(self.driver)


    #返回短信内容实例化对象
    def get_recriver(self):
        return RecriverPage(self.driver)