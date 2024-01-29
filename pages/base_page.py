from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator, s):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()
        print("Clicking: ", s)

    def set(self, locator, value, s):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

        print("Populating: ", s)

    def enter(self, locator, value, s):
        element = (WebDriverWait(self.driver, 20)
                   .until(EC.element_to_be_clickable(locator)))
        ActionChains(self.driver) \
            .click(element) \
            .pause(1) \
            .send_keys(value) \
            .pause(1) \
            .send_keys(Keys.TAB) \
            .perform()
        print("Populating: ", s)

    def enter_tab(self, locator, value):
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.element_to_be_clickable(locator)))
        actions = ActionChains(self.driver) \
            .click(element) \
            .pause(1) \
            .send_keys(value)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def dropdown(self, locator, value, s):
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.element_to_be_clickable(locator)))
        element.click()
        ul_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='select2-results__options']")))
        li_item = ul_item.find_element(By.XPATH, f".//li[text()='{value}']")
        ActionChains(self.driver) \
            .click(li_item) \
            .pause(1) \
            .perform()

        print("Selecting: ", s)

    def notification_message_is_displayed(self, message):
        is_message_displayed = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f".//h3[text()='{message}']")))
        return is_message_displayed.is_displayed()

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title
