from base_class.base_form import BaseForm
from elements.button import Button
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging


class MainPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Main"
        self.__main_banner_btn = Button("//div[@class='home-banner']", "Join us button")
        self.__alerts_frame_window_btn = Button("//h5[contains(text(), 'Alerts')]",
                                           "Alerts, frames & windows page open button")
        self.__elements_page_btn = Button("//h5[contains(text(), 'Elements')]", "Elements page open button")
        self.__widgets_page_btn = Button("//h5[contains(text(), 'Widgets')]", "Widgets page open button")
        super().__init__(self.__main_banner_btn, self.__name_of_the_page)

    def open_the_alerts_frames_windows_page(self):
        Logging.write_log_info("Open the Alerts, frames & windows page")
        target = self.__alerts_frame_window_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__alerts_frame_window_btn.click_on_the_element()

    def open_the_elements_page(self):
        Logging.write_log_info("Open the Elements page")
        target = self.__elements_page_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__elements_page_btn.click_on_the_element()

    def open_the_widgets_page(self):
        Logging.write_log_info("Open the Widgets page")
        target = self.__widgets_page_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__widgets_page_btn.click_on_the_element()
