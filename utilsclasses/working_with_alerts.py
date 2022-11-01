from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from browser_utils.singleton import Singleton
from utilsclasses.logger import Logging


class Alerts:

    def __init__(self):
        self.alert = WebDriverWait(Singleton.get_instance().driver, 5).until(ec.alert_is_present())

    def click_the_accept(self):
        Logging.write_log_info("Closing alert box")
        self.alert.accept()

    def click_the_dismiss(self):
        Logging.write_log_info("Closing alert box")
        self.alert.dismiss()

    def send_keys_and_accept(self, keys):
        Logging.write_log_info("Send text and close prompt alert box")
        self.alert.send_keys(keys)
        self.alert.accept()

    def get_the_text_from_alert(self):
        text = self.alert.text
        return text

    @staticmethod
    def check_alert_box_is_closed():
        try:
            alert = Alerts()
            return False
        except TimeoutException:
            return True
