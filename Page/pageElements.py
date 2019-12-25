from selenium.webdriver.common.by import By


class PageElements:
    """新增短信页面"""
    # 添加
    add_message_btn_id = (By.ID, "com.android.mms:id/action_compose_new")

    """短信发送页面"""
    # 接受者
    recriver_btn_xpath = (By.XPATH, "//*[contains(@text,'接收者')]")
    # 内容
    add_text_btn_xpath = (By.XPATH, "//*[contains(@text,'键入信息')]")
    # 发送
    click_on_btn_id = (By.ID, "com.android.mms:id/send_button_sms")
    # 获取当前页面信息
    text_ids = (By.ID, "com.android.mms:id/text_view")
