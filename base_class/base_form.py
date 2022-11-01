from utilsclasses.config_manager import WorkingWithData
from utilsclasses.logger import Logging


class BaseForm:

    waits = WorkingWithData.working_with_data("waits", "config")

    def __init__(self, unique_element, name_page):
        self.unique_element = unique_element
        self.name_page = name_page

    def is_page_open(self):
        Logging.write_log_info(f"Checking is {self.name_page} page open")
        return self.unique_element.element_is_displayed()

    def get_the_page_name(self):
        return self.name_page
