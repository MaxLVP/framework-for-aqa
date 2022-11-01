from browser_utils.singleton import Singleton
from utilsclasses.config_manager import WorkingWithData
from browser_utils.js_constants import SCROLL_TO_TARGET


class DriverUtils:

    def __init__(self):
        self.driver = Singleton.get_instance().driver

    def navigate_to_url(self):
        url = WorkingWithData.working_with_data("url", "config")
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def switch_to_tab(self, tab_name):
        self.driver.switch_to.window(tab_name)

    def get_the_list_of_window_handles(self):
        return self.driver.window_handles

    def get_the_window_handle(self):
        return self.driver.current_window_handle

    def execute_js_script_to_scroll(self, target):
        self.driver.execute_script(SCROLL_TO_TARGET, target)

    @staticmethod
    def clear_driver_instance():
        Singleton._instances = {}
