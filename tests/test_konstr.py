import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import  Constants
from constants import  URLs

class TestKonstr():


    # чтобы проверить переход на таб булки, сначала нужно с него уйти и потом вернуться.
    def test_konstr_bulki_true(self, driver):
        driver.find_element(*Locators.sous_button_main_page).click()
        parent_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.bulki_buuton_main_page))
        parent_element.click()
        assert "tab_tab_type_current__2BEPc" in parent_element.get_attribute("class")


    def test_konstr_sous_true(self, driver):
        parent_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.sous_button_main_page))
        parent_element.click()
        assert "tab_tab_type_current__2BEPc" in parent_element.get_attribute("class")

    def test_konstr_nachinki_true(self, driver):
        parent_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.nachinki_button_main_page))
        parent_element.click()
        assert "tab_tab_type_current__2BEPc" in parent_element.get_attribute("class")




