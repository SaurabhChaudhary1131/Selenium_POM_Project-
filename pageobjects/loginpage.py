class Login:
    textbox_username_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[@type='submit']"
    button_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element("xpath",self.textbox_username_xpath).clear()
        self.driver.find_element("xpath", self.textbox_username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element("xpath",self.textbox_password_xpath).clear()
        self.driver.find_element("xpath", self.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element("xpath",self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element("xpath",self.button_logout_xpath).click()

