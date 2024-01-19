from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LandingPage(BasePage):

    member_transactions = (By.XPATH, "//a[text()='Member Transactions']")
    sell_insurance = (By.XPATH, "(//a[@class='subnav-item'])[5]")
    sell_insurance_link = (By.XPATH, "(//a[@class='navbar-item'])[15]")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_header(self):
        self.click(self.member_transactions)
        self.click(self.sell_insurance)
        self.click(self.sell_insurance_link)





