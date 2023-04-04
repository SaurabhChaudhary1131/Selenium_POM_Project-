import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageobjects.loginpage import Login
from utilities.read_properties import Readconfig
class Test_001_login:
    baseurl = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    def test_homepage(self):
        global s
        s = Service("C:\\Users\\saurabh.chaudhary\\PycharmProjects\\nopcommerceApp\\Chromedriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        title=self.driver.title
        if title == "Your store. Login1":
            #jut remove 1 after login and test will run good.
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "s.png")
            self.driver.close()
            assert False


    def test_login(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.obj=Login(self.driver)
        self.obj.setusername(self.username)
        self.obj.setpassword(self.password)
        self.obj.clicklogin()
        self.driver.close()









