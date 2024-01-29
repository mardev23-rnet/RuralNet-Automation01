import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ChoosePlan(BasePage):
    oph_offers = (By.XPATH, "//a[@data-target='box-GTLHFFLI12']")
    fortunelife_group_term_life_insurance2 = (By.XPATH, "(//a[@class='button is-small is-darkblue'])[25]")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_fortunelife_groupterm_lifeinsurance2(self):
        self.click(self.oph_offers, "OPH Offers")
        time.sleep(3)
        self.click(self.fortunelife_group_term_life_insurance2, "FortuneLife Group-Term Life Insurance 2")
        time.sleep(3)
