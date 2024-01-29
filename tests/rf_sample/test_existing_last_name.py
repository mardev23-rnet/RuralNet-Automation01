import time

from pages.login_page import LoginPage
from pages.navbar_menu_page import NavBarMenu
from pages.choose_plan_page import ChoosePlan
from pages.sell_insurance_page import SellInsurancePage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestExistingRecords(BaseTest):
    def test_confirm_error_existing_member(self):
        login_page = LoginPage(self.driver)
        login_page.skip_announcement()
        login_page.set_email_address(TestData.user)
        login_page.set_password(TestData.password)
        login_page.click_login_button()

        navbar_menu = NavBarMenu(self.driver)
        navbar_menu.click_sell_insurance_submenu()

        choose_plan = ChoosePlan(self.driver)
        choose_plan.choose_fortunelife_groupterm_lifeinsurance2()

        sell_insurance_page = SellInsurancePage(self.driver)
        sell_insurance_page.sell_to_existing_record(TestData.insured_lastname,
                                                    TestData.insured_firstname,
                                                    TestData.insured_middlename,
                                                    TestData.insured_date_of_birth,
                                                    TestData.insured_gender,
                                                    TestData.message,
                                                    TestData.insured_phone_number)
