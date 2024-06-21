from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestKonstr():

    def common_meth(self, driver, locator):
        parent_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator))
        if not "tab_tab_type_current__2BEPc" in parent_element.get_attribute("class"):
            parent_element.click()
        else:
            pass
        assert "tab_tab_type_current__2BEPc" in parent_element.get_attribute("class")

    def test_konstr_bulki_true(self, driver):
        self.common_meth(driver, Locators.bulki_buuton_main_page)

    def test_konstr_sous_true(self, driver):
        self.common_meth(driver, Locators.sous_button_main_page)

    def test_konstr_nachinki_true(self, driver):
        self.common_meth(driver, Locators.nachinki_button_main_page)




