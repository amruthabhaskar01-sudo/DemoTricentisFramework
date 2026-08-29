from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):

    login_link = (By.LINK_TEXT, "Log in")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH,'(//input[@type="submit"])[2]')

    def click_login(self):
        self.click(self.login_link)

    def enter_email(self,email):
        self.enter_text(self.email,email)

    def enter_password(self,password):
        self.enter_text(self.password,password)

    def click_login_button(self):
        self.click(self.login_button)
