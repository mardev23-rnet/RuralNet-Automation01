from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SellInsurancePage(BasePage):
    insured_last_name_field = (By.XPATH, "//input[@id='firstString']")
    insured_first_name_field = (By.XPATH, "//input[@id='string1']")
    insured_middle_name_field = (By.XPATH, "//input[@id='string2']")
    insured_date_of_birth_field = (By.XPATH, "//input[@id='date1']")
    select_gender_option = (
        By.XPATH, "(//span[@class='select2-selection__arrow'])[1]")
    insured_phone_number_field = (By.XPATH, "//input[@id='firstCellNo']")
    insured_address_field = (By.XPATH, "//input[@id='string3']")
    province_option = (By.XPATH, "//select[@id='select1']")
    civil_status_option = (By.XPATH, "//span[@id='select2-selectGo3-container']")
    insured_occupation_field = (By.XPATH, "//input[@id='string4']")
    insured_place_of_birth_field = (By.XPATH, "//input[@id='string5']")
    insured_sss_tin_field = (By.XPATH, "//input[@id='string6']")
    bene_last_name_field = (By.XPATH, "//input[@id='string7']")
    bene_first_name_field = (By.XPATH, "//input[@id='string8']")
    bene_middle_name_field = (By.XPATH, "//input[@id='string9']")
    bene_relationship_option = (By.XPATH, "//span[@id='select2-select4-container']")
    amount_recieved_field = (By.XPATH, "//input[@id='currency47']")
    family_lastname_field = (By.XPATH, "//input[@id='string201']")
    family_firstname_field = (By.XPATH, "//input[@id='string211']")
    family_middlename_field = (By.XPATH, "//input[@id='string221']")
    family_dateofbirth_field = (By.XPATH, "//input[@id='date21']")
    family_relationship_field = (By.XPATH, "//span[@id='select2-select91-container']")
    referrer_option = (By.XPATH, "//select[@id='select8']")
    reference_client_id_field = (By.XPATH, "//input[@id='stringGo91']")
    confirm_notcombatantduties_tickbox = (By.XPATH, "//input[@class='cm-checkbox confirm1-checkbox1']")
    confirm_termsandcondition_tickbox = (By.XPATH, "//input[@class='cm-checkbox confirm-checkbox']")
    pay_complete_transaction_button = (By.XPATH, "//button[text()='Pay & Complete Transaction']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_insurance_form(self,
                            insured_lastname,
                            insured_firstname,
                            insured_middlename,
                            insured_date_of_birth,
                            insured_gender,
                            insured_phone_number,
                            insured_address,
                            insured_province,
                            insured_civil_status,
                            insured_occupation,
                            insured_place_of_birth,
                            insured_sss_tin,
                            bene_lastname,
                            bene_firstname,
                            bene_middlename,
                            bene_relationship,
                            amount_recieved,
                            family_lastname,
                            family_firstname,
                            family_middlename,
                            family_dateofbirth,
                            family_relationship,
                            reference_client_id):
        self.wait_for_element_to_be_visible(self.insured_last_name_field)
        self.set(self.insured_last_name_field, insured_lastname)
        self.set(self.insured_first_name_field, insured_firstname)
        self.set(self.insured_middle_name_field, insured_middlename)
        self.set(self.insured_date_of_birth_field, insured_date_of_birth)

        # Gender Selection
        self.click(self.select_gender_option)
        gender = (By.XPATH, f"//option[text()='{insured_gender}']")
        self.click(gender)

        self.driver.implicit_wait(500)
        self.set(self.insured_phone_number_field, insured_phone_number)
        self.set(self.insured_address_field, insured_address)

        # Province Selection
        self.click(self.province_option)
        province = By.XPATH, f"//option[text()='{insured_gender}']"
        self.click(province)

        # Civil Status Selection
        self.click(self.civil_status_option)
        civil_status = By.XPATH, "//li[text()=" + insured_civil_status + "]"
        self.click(civil_status)

        self.set(self.insured_occupation_field, insured_occupation)
        self.set(self.insured_place_of_birth_field, insured_place_of_birth)
        self.set(self.insured_sss_tin_field, insured_sss_tin)

        self.set(self.bene_last_name_field, bene_lastname)
        self.set(self.bene_first_name_field, bene_firstname)
        self.set(self.bene_middle_name_field, bene_middlename)

        # Beneficiary Relationship Selection
        self.click(self.bene_relationship_option)
        relationship_beneficiary = By.XPATH, "//li[text()=" + bene_relationship + "]"
        self.click(relationship_beneficiary)

        self.set(self.amount_recieved_field, amount_recieved)

        self.set(self.family_lastname_field, family_lastname)
        self.set(self.family_firstname_field, family_firstname)
        self.set(self.family_dateofbirth_field, family_dateofbirth)
        self.set(self.family_middlename_field, family_middlename)

        # Family Relationship Selection
        self.click(self.family_relationship_field)
        relationship_family = By.XPATH, "//li[text()=" + family_relationship + "]"
        self.click(relationship_family)

        self.set(self.reference_client_id_field, reference_client_id)

        self.click(self.confirm_notcombatantduties_tickbox)
        self.click(self.confirm_termsandcondition_tickbox)

        self.click(self.pay_complete_transaction_button)
