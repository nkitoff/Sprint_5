import pytest
from selenium import webdriver
import constants
from locators import Locators
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
faker = Faker()


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.lk_button_in_head)).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.auth_header_auth_page))
    driver.find_element(*Locators.email_input_auth_and_regist_page).send_keys(constants.CORRECT_EMAIL)
    driver.find_element(*Locators.password_input_auth_and_registr).send_keys(constants.CORRECT_PASSWORD)
    driver.find_element(*Locators.auth_button_auth_page).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.main_header_main_page))
    return driver

