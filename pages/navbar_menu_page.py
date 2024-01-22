from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NavBarMenu(BasePage):
    member_transactions = (By.XPATH, "//a[text()='Member Transactions']")
    sell_insurance = (By.XPATH, "(//a[@class='subnav-item'])[5]")
    sell_insurance_sellinsurance = (By.XPATH, "(//a[@class='navbar-item'])[15]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sell_insurance_submenu(self):
        self.click(self.member_transactions)
        self.click(self.sell_insurance)
        self.click(self.sell_insurance_sellinsurance)
