from appium import webdriver


def get_android_driver(pac, act):
    capabilities = {
        "platformName": "Android",  # 操作平台(Android和iOS
        "platformVersion": "5.1",  # 设备系统版本号
        "deviceName": "模拟器",  # 设备名称
        "appPackage": pac,  # 待测应用的包名
        "appActivity": act  # 待测应用的启动名
    }
    # 返回driver驱动对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
