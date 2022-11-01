from base_class.base_form import BaseForm
from elements.button import Button
from elements.textfield import TextField
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging


class WidgetsPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Widgets"
        self.__header_of_page = TextField("//div[contains(text(), 'Widgets') and contains(@class, 'main-header')]",
                                     "Header of Widgets page")
        self.__date_picker_page_btn = Button("//span[text()='Date Picker']", "Date Picker page button")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def open_the_data_picker_page(self):
        Logging.write_log_info("Open the Date Picker page")
        target = self.__date_picker_page_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__date_picker_page_btn.click_on_the_element()
