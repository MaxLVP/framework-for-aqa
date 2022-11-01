from browser_utils.singleton import Singleton
from selenium.webdriver.common.by import By
from utilsclasses.logger import Logging


class BaseElement:

    def __init__(self, locator, name_of_element):
        self.locator = locator
        self.name_of_element = name_of_element
        self.driver = Singleton.get_instance().driver

    def find_element(self):
        Logging.write_log_debug(f"Finding element {self.name_of_element}")
        return self.driver.find_element(By.XPATH, self.locator)

    def find_elements(self):
        Logging.write_log_debug(f"Finding list of elements by locator: {self.locator}")
        return self.driver.find_elements(By.XPATH, self.locator)

    def click_on_the_element(self):
        Logging.write_log_debug(f"Click on the element {self.name_of_element}")
        BaseElement.find_element(self).click()

    def get_text_from_element(self):
        Logging.write_log_debug(f"Getting text from {self.name_of_element} element")
        return BaseElement.find_element(self).text

    def element_is_displayed(self):
        Logging.write_log_debug(f"Checking if {self.name_of_element} displayed")
        return BaseElement.find_element(self).is_displayed()

    def get_the_attribute_value(self, attribute):
        Logging.write_log_debug(f"Getting attribute: {attribute} from {self.name_of_element} element")
        return BaseElement.find_element(self).get_attribute(attribute)

