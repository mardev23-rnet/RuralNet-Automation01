from pages.login_page import LoginPage
from pages.navbar_menu_page import NavBarMenu
from pages.choose_plan_page import ChoosePlan
from pages.sell_insurance_page import SellInsurancePage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestSellInsurance(BaseTest):

    def test_fillup_insurance_form(self):
        login_page = LoginPage(self.driver)
        login_page.skip_announcement()
        login_page.set_email_address(TestData.user)
        login_page.set_password(TestData.password)
        login_page.click_login_button()

        nav_menu = NavBarMenu(self.driver)
        nav_menu.click_sell_insurance_submenu()

        choose_plan_page = ChoosePlan(self.driver)
        choose_plan_page.choose_fortunelife_groupterm_lifeinsurance2()

        sell_insurance_page = SellInsurancePage(self.driver)
        sell_insurance_page.fill_insurance_form(TestData.insured_lastname, TestData.insured_firstname, TestData.insured_middlename,
                                                TestData.insured_date_of_birth, TestData.insured_gender, TestData.insured_phone_number,
                                                TestData.insured_address, TestData.insured_province, TestData.insured_civil_status,
                                                TestData.insured_occupation, TestData.insured_place_of_birth, TestData.insured_sss_tin,
                                                TestData.bene_lastname, TestData.bene_firstname, TestData.bene_middlename,
                                                TestData.bene_relationship, TestData.amount_recieved, TestData.family_lastname,
                                                TestData.family_firstname, TestData.family_middlename,TestData.family_relationship,
                                                TestData.family_dateofbirth, TestData.reference_client_id)
