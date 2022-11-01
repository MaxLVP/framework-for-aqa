from base_class.base_form import BaseForm
from elements.button import Button
from elements.textfield import TextField
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging


class ElementsPage(BaseForm):

    def __init__(self):

        self.__name_of_the_page = "Elements"
        self.__header_of_page = TextField("//div[contains(text(), 'Elements') and contains(@class, 'main-header')]",
                                     "Header of Elements page")
        self.__web_tables_page_open_btn = Button("//span[text()='Web Tables']", "Web tables page open button")
        self.__upload_page_open_btn = Button("//span[text()='Upload and Download']", "Upload and Download page open button")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def open_the_web_tables_page(self):
        Logging.write_log_info(f"Open the Web Tables page")
        target = self.__web_tables_page_open_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__web_tables_page_open_btn.click_on_the_element()

    def open_the_upload_and_download_page(self):
        Logging.write_log_info("Open the Upload and Download page")
        target = self.__upload_page_open_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__upload_page_open_btn.click_on_the_element()
