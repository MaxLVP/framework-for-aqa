from elements.base_element import BaseElement
from utilsclasses.logger import Logging


class Input(BaseElement):

    def __init__(self, locator, name_of_element):
        super().__init__(locator, name_of_element)

    def send_value(self, value):
        Logging.write_log_info(f"Send the {value} to the {self.name_of_element}")
        self.find_element().send_keys(value)
