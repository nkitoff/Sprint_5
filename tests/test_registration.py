import time
import random
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators
faker = Faker()

class TestRegistration():
    def generate_random_data(self):
        random_email = faker.email()
        random_name = faker.name()
        random_password_correct = random.randint(100000, 999999)
        random_password_incorrect = random.randint(0,99999)
        return random_email, random_name, random_password_correct, random_password_incorrect

    def type_registr_data(self,driver,type):
        random_email, random_name, random_password_correct, random_password_incorrect = self.generate_random_data()
        driver.find_element(*Locators.auth_button_main_page).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.auth_header_auth_page))
        driver.find_element(*Locators.registr_button_auth_page).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.registr_header_regist_page))
        driver.find_element(*Locators.name_input_regist_page).send_keys(random_name)
        driver.find_element(*Locators.email_input_auth_and_regist_page).send_keys(random_email)
        if type == "correct":
            driver.find_element(*Locators.password_input_auth_and_registr).send_keys(random_password_correct)
        elif type == "incorrect":
            driver.find_element(*Locators.password_input_auth_and_registr).send_keys(random_password_incorrect)
        driver.find_element(*Locators.registr_button_regist_page).click()

    def test_registration_true(self,driver):
        self.type_registr_data(driver,"correct")
        final_text_h2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.auth_header_auth_page)).text
        assert final_text_h2 == constants.MAIN_HEADER_AUTH_PAGE_TEXT

    def test_registration_false(self, driver):
        self.type_registr_data(driver, "incorrect")
        message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.incorrect_pass_registr_page)).text
        assert message == constants.INCORRECT_PASS_AUTH_PAGE_MESS
