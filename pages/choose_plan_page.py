from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ChoosePlan(BasePage):
    oph_offers = (By.XPATH, "//a[@data-target='box-GTLHFFLI12']")
    fortunelife_group_term_life_insurance2 = \
        (By.XPATH, "(//a[@href='MenuForm.htm?programName=INS_SellInsurance&formType=InsuranceForm&calledFrom=INS_SelectProduct&primaryKey=GTLHF:FLI11'])[3]")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_fortunelife_groupterm_lifeinsurance2(self):
        self.click(self.oph_offers)
        self.wait_for_element_to_be_visible(self.fortunelife_group_term_life_insurance2)
        self.click(self.fortunelife_group_term_life_insurance2)
