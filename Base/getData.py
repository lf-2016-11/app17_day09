import os,yaml
class GetData:
    """解析数据"""
    def get_yml_data(self,yml_name):
        """
        返回yml文件数据
        :param yml_name:  yaml数据文件名字
        :return:
        """
        # 读n os.sep:获取系统路径分隔符 因为unix分隔符为:"/",window为"\"
        with open("./Data" + os.sep + yml_name, "r", encoding="utf-8") as f:
            # 解析
            return yaml.safe_load(f)