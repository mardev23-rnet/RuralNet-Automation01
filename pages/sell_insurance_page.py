import time
from selenium.webdriver.common.by import By
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
    province_option = (By.XPATH, "(//span[@class='select2-selection__arrow'])[2]")
    civil_status_option = (By.XPATH, "(//span[@class='select2-selection__arrow'])[3]")
    insured_occupation_field = (By.XPATH, "//input[@id='string4']")
    insured_place_of_birth_field = (By.XPATH, "//input[@id='string5']")
    insured_sss_tin_field = (By.XPATH, "//input[@id='string6']")
    bene_last_name_field = (By.XPATH, "//input[@id='string7']")
    bene_first_name_field = (By.XPATH, "//input[@id='string8']")
    bene_middle_name_field = (By.XPATH, "//input[@id='string9']")
    bene_relationship_option = (By.XPATH, "(//span[@class='select2-selection__arrow'])[4]")
    amount_recieved_field = (By.XPATH, "//input[@id='currency47']")
    family_lastname_field = (By.XPATH, "//input[@id='string201']")
    family_firstname_field = (By.XPATH, "//input[@id='string211']")
    family_middlename_field = (By.XPATH, "//input[@id='string221']")
    family_dateofbirth_field = (By.XPATH, "//input[@id='date21']")
    family_relationship_field = (By.XPATH, "(//span[@class='select2-selection__arrow'])[8]")
    referrer_option = (By.XPATH, "//select[@id='select8']")
    reference_client_id_field = (By.XPATH, "//input[@id='stringGo19']")
    confirm_notcombatantduties_tickbox = (By.XPATH, "(//label[@class='cm-checkbox'])[3]")
    confirm_termsandcondition_tickbox = (By.XPATH, "(//label[@class='cm-checkbox'])[4]")
    pay_complete_transaction_button = (By.XPATH, "//button[@value='Pay & Complete Transaction']")

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
                            family_relationship,
                            family_dateofbirth,
                            reference_client_id):
        self.set(self.insured_last_name_field,
                 insured_lastname,
                 "Insured Last Name field")

        self.set(self.insured_first_name_field, insured_firstname, "Insured First Name")
        self.set(self.insured_middle_name_field, insured_middlename, "Insured Middle Name")
        self.set(self.insured_date_of_birth_field, insured_date_of_birth, "Insured Date of Birth")
        self.dropdown(self.select_gender_option, insured_gender, "Insured Gender")
        self.set(self.insured_phone_number_field, insured_phone_number, "Insured Phone")
        self.set(self.insured_address_field, insured_address, "Insured Address")
        self.dropdown(self.province_option, insured_province, "Insured Province")
        self.dropdown(self.civil_status_option, insured_civil_status, "Insured Civil Status")
        time.sleep(3)
        self.set(self.insured_occupation_field, insured_occupation, "Insured Occupation")
        self.set(self.insured_place_of_birth_field, insured_place_of_birth, "Insured Place of Birth")
        self.set(self.insured_sss_tin_field, insured_sss_tin, "Insured SSS/TIN")
        self.set(self.bene_last_name_field, bene_lastname, "Beneficiary Last Name")
        self.set(self.bene_first_name_field, bene_firstname, "Beneficiary First Name")
        self.set(self.bene_middle_name_field, bene_middlename, "Beneficiary Middle Name")
        self.dropdown(self.bene_relationship_option, bene_relationship, "Beneficiary Relationship")
        self.enter(self.amount_recieved_field, amount_recieved, "Amount Received")
        self.set(self.family_lastname_field, family_lastname, "Family Last Name")
        self.set(self.family_firstname_field, family_firstname, "Family First Name")
        self.set(self.family_middlename_field, family_middlename, "Family Middle Name")
        self.dropdown(self.family_relationship_field, family_relationship, "Family Relationship")
        self.enter(self.family_dateofbirth_field, family_dateofbirth, "Family Date of Birth")
        time.sleep(5)
        self.click(self.confirm_notcombatantduties_tickbox, "Agreement for non-combatant service")
        self.click(self.confirm_termsandcondition_tickbox, "Agreement in Terms and Condition")
        self.click(self.pay_complete_transaction_button, "Pay and Complete Transaction")

    def sell_to_existing_record(self, insured_firstname, insured_lastname, insured_middlename, insured_date_of_birth,
                                insured_gender, message, insured_phone_number):
        print("Message", message)
        self.set(self.insured_last_name_field,
                 insured_lastname,
                 "Insured Last Name field")
        self.set(self.insured_first_name_field, insured_firstname, "Insured First Name")
        self.set(self.insured_middle_name_field, insured_middlename, "Insured Middle Name")
        self.set(self.insured_date_of_birth_field, insured_date_of_birth, "Insured Date of Birth")
        self.dropdown(self.select_gender_option, insured_gender, "Insured Gender")
        assert True == self.notification_message_is_displayed(message)
