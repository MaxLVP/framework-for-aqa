from base_class.base_form import BaseForm
from elements.textfield import TextField
from elements.button import Button
from browser_utils.singleton import Singleton
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BrowserWindows(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Browser Windows"
        self.__header_of_page = TextField("//div[contains(text(), 'Browser') and contains(@class, 'main-header')]",
                                     "Header of Browser Windows page")
        self.__new_tab_btn = Button("//button[@id='tabButton']", "New tab open button")
        self.__elements_submenu_open_btn = Button("//div[contains(text(), 'Elements')]", "Elements submenu open button")
        self.__links_page_open_btn = Button("//span[text() = 'Links']", "Links page open button")
        self.__new_tab_text_filed = TextField("//h1[@id='sampleHeading']", "New tab header")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def open_new_tab(self):
        Logging.write_log_info("Open a new tab")
        original_tab = Singleton.get_instance().driver.current_window_handle
        self.__new_tab_btn.click_on_the_element()
        waits = WebDriverWait(Singleton.get_instance().driver, BrowserWindows.waits).until(ec.number_of_windows_to_be(2))
        for current_tab in Singleton.get_instance().driver.window_handles:
            DriverUtils().switch_to_tab(current_tab)
            headers = self.__new_tab_text_filed.find_elements()
            if len(headers) > 0:
                Singleton.get_instance().driver.close()
                break
        DriverUtils().switch_to_tab(original_tab)
        return True

    def open_links_page(self):
        Logging.write_log_info(f"Open Links page")
        self.__elements_submenu_open_btn.click_on_the_element()
        waits = WebDriverWait(Singleton.get_instance().driver, BrowserWindows.waits).until(ec.element_to_be_clickable(self.__links_page_open_btn.find_element()))
        target = self.__links_page_open_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__links_page_open_btn.click_on_the_element()
