from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SellInsurancePage(BasePage):
    oph_klpp_button = (By.XPATH, "//span[text()='Apply']")
    insured_last_name_field = (By.XPATH, "//input[@id='firstString']")
    first_name_field = (By.XPATH, "//input[@id='string1']")
    middle_name_field = (By.XPATH, "//input[@id='string2']")
    date_of_birth_field = (By.XPATH, "//input[@id='date1']")
    select_gender_option = (
        By.XPATH, "//span[@class='select2 select2-container select2-container--default select2-container--below']")
    phone_number_field = (By.XPATH, "//input[@name='insuredCellNo']")
    address_field = (By.XPATH, "//input[@id='string3']")
    province_option = (By.XPATH, "//select[@id='select1']")
    civil_status_option = (By.XPATH, "//span[@id='select2-selectGo3-container']")
    occupation_field = (By.XPATH, "//input[@id='string4']")
    place_of_birth_field = (By.XPATH, "//input[@id='string5']")
    sss_tin_field = (By.XPATH, "//input[@id='string6']")
    bene_last_name_field = (By.XPATH, "//input[@id='string7']")
    bene_first_name_field = (By.XPATH, "//input[@id='string8']")
    bene_middle_name_field = (By.XPATH, "//input[@id='string9']")
    bene_relationship_option = (By.XPATH, "//span[@id='select2-select4-container']")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_plan(self):
        self.click(self.oph_klpp_button)
