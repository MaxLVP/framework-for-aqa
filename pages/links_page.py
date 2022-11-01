from base_class.base_form import BaseForm
from elements.textfield import TextField
from elements.button import Button
from browser_utils.singleton import Singleton
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Links(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Links"
        self.__header_of_page = TextField("//div[contains(text(), 'Links') and contains(@class, 'main-header')]",
                                     "Header of Links page")
        self.__home_link_btn = Button("//a[@id='simpleLink']", "Home page link")
        self.__main_banner_btn = Button("//div[@class='home-banner']", "Join us button")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def open_the_home_page(self):
        Logging.write_log_info(f"Open the Main page from Links page")
        target = self.__home_link_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__home_link_btn.click_on_the_element()
        __wait = WebDriverWait(Singleton.get_instance().driver, Links.waits)
        waits = __wait.until(ec.number_of_windows_to_be(2))
        for current_tab in DriverUtils().get_the_list_of_window_handles():
            DriverUtils().switch_to_tab(current_tab)
            headers = self.__main_banner_btn.find_elements()
            if len(headers) > 0:
                break

    def resume_to_previous_tab(self):
        Logging.write_log_info("Resume a previous tab")
        for current_tab in DriverUtils().get_the_list_of_window_handles():
            DriverUtils().switch_to_tab(current_tab)
            headers = self.__header_of_page.find_elements()
            if len(headers) > 0:
                break
