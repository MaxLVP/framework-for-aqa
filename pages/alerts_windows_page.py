from base_class.base_form import BaseForm
from elements.button import Button
from elements.textfield import TextField
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging


class AlertsWindowsPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Alerts, frames & windows"
        self.__header_of_page = TextField("//div[contains(text(), 'Alerts,') and contains(@class, 'main-header')]",
                                     "Header of Alerts, frames & windows page")
        self.__alerts_btn = Button("//span[contains(text(), 'Alerts')]", "Alerts page open button")
        self.__nested_frames_btn = Button("//span[contains(text(), 'Nested')]", "Nested frames page open button")
        self.__frames_btn = Button("//span[text()='Frames']", "frames")
        self.__browser_windows_btn = Button("//span[contains(text(), 'Browser')]", "Browser windows page open button")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def click_the_alerts_btn(self):
        Logging.write_log_info(f"Open the Alerts page")
        target = self.__alerts_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__alerts_btn.click_on_the_element()

    def click_the_nested_frames_btn(self):
        Logging.write_log_info(f"Open the Nested Frames page")
        target = self.__nested_frames_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__nested_frames_btn.click_on_the_element()

    def click_the_browser_windows_btn(self):
        Logging.write_log_info("Open the Browser Windows page")
        self.__browser_windows_btn.click_on_the_element()
