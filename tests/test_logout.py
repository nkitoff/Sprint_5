from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators
from constants import  Constants
from constants import  URLs

class TestLogout():

    def test_logout_true(self,login):
        driver = login
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.lk_button_in_head)).click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable(Locators.logout_button_lk_page)).click()
        current_url = driver.current_url
        page_header = WebDriverWait(driver,20).until(EC.visibility_of_element_located((Locators.auth_header_auth_page))).text
        assert current_url == URLs.URL_LK_PAGE and page_header == Constants.MAIN_HEADER_AUTH_PAGE_TEXT