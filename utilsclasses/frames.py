from browser_utils.singleton import Singleton
from selenium.webdriver.common.by import By
from utilsclasses.logger import Logging


class Frames:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def find_frame(self):
        return Singleton.get_instance().driver.find_element(By.XPATH, self.locator)

    def switch_to_frame(self):
        Logging.write_log_info(f"Switching to {self.name} frame")
        Singleton.get_instance().driver.switch_to.frame(self.find_frame())
