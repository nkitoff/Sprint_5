from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import  Constants
from constants import  URLs

class TestLk():

    def test_lk_true(self,login):
        driver = login
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.lk_button_in_head)).click()
        lk_email_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.email_field_lk_page))
        lk_email = lk_email_element.get_attribute("value")
        current_url = driver.current_url
        assert lk_email == Constants.CORRECT_EMAIL and current_url == URLs.URL_LK_PAGE



