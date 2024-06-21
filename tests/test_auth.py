from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators

class TestAuth():

    def type_data(self,driver):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.auth_header_auth_page))
        driver.find_element(*Locators.email_input_auth_and_regist_page).send_keys(constants.CORRECT_EMAIL)
        driver.find_element(*Locators.password_input_auth_and_registr).send_keys(constants.CORRECT_PASSWORD)
        driver.find_element(*Locators.auth_button_auth_page).click()
        return driver

    def check_email_lk_page(self,driver):
        WebDriverWait(driver,20).until(EC.visibility_of_element_located(Locators.main_header_main_page))
        driver.find_element(*Locators.lk_button_in_head).click()
        lk_email_element = WebDriverWait(driver,20).until(EC.visibility_of_element_located(Locators.email_field_lk_page))
        lk_email = lk_email_element.get_attribute("value")
        assert lk_email == constants.CORRECT_EMAIL
        return driver


    def test_auth_login_button_main_page_true(self,driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.auth_button_main_page)).click()
        self.type_data(driver)
        self.check_email_lk_page(driver)

    def test_auth_lk_button_true(self,driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.lk_button_in_head)).click()
        self.type_data(driver)
        self.check_email_lk_page(driver)

    def test_auth_registr_page_true(self,driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.auth_button_main_page)).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.auth_header_auth_page))
        driver.find_element(*Locators.registr_button_auth_page).click()
        driver.find_element(*Locators.auth_button_registr_and_restore_page).click()
        self.type_data(driver)
        self.check_email_lk_page(driver)

    def test_auth_restore_password_page(self,driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.auth_button_main_page)).click()
        driver.find_element(*Locators.restore_password_auth_page).click()
        driver.find_element(*Locators.auth_button_registr_and_restore_page).click()
        self.type_data(driver)
        self.check_email_lk_page(driver)


