
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators


class TestLkToConstr():

    def test_lk_to_constr_true(self,login):
        driver = login
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.lk_button_in_head)).click()
        driver.find_element(*Locators.konstr_button_in_head).click()
        main_head_text = WebDriverWait(driver,20).until(EC.visibility_of_element_located(Locators.main_header_main_page)).text
        assert main_head_text == constants.MAIN_HEADER_MAIN_PAGE_TEXT

    def test_lk_to_head_button_true(self, login):
        driver = login
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.lk_button_in_head)).click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable(Locators.main_button_in_header)).click()
        main_head_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.main_header_main_page)).text
        assert main_head_text == constants.MAIN_HEADER_MAIN_PAGE_TEXT