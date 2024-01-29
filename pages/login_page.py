import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
# from pages.my_account_page import MyAccountPage


class LoginPage(BasePage):
    next_button = (By.XPATH, "//button[@class='swal2-confirm swal2-styled']")
    username_field = (By.XPATH, "//input[@id='loginName']")
    password_field = (By.XPATH, "//input[@id='password']")
    year_field = (By.XPATH, "//input[@id='year']")
    login_button = (By.XPATH, "//button[@name='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def skip_announcement(self):
        self.click(self.next_button, "Skip Announcement")
        time.sleep(3)
        self.click(self.next_button, "Skip Announcement")

    def set_email_address(self, username):
        self.set(self.username_field, username, "Login Name")
        # self.driver.find_element(self.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.set(self.password_field, password, "Password")

    def click_login_button(self):
        self.click(self.login_button, "Login Button")
        # return MyAccountPage(self.driver)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

