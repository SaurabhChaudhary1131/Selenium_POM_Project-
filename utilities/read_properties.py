import configparser
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig:
    @staticmethod
    def geturl():
        url = config.get("common_info","baseurl")
        return url

    @staticmethod
    def getusername():
        username = config.get("common_info", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common_info", "password")
        return password