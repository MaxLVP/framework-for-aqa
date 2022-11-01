from base_class.base_form import BaseForm
from elements.button import Button
from elements.textfield import TextField
from utilsclasses.logger import Logging


class AlertsPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Alerts"
        self.__header_of_page = TextField("//div[contains(text(), 'Alerts') and contains(@class, 'main-header')]",
                                     "Header of Alerts page")
        self.__button_to_see_alert = Button("//button[@id='alertButton']", "Alert box open button")
        self.__button_to_open_confirm_box = Button("//button[@id='confirmButton']", "Confirm box open button")
        self.__result_of_confirm_box = TextField("//span[@id='confirmResult']", "Textfield with text from confirm box")
        self.__button_to_open_prompt_box = Button("//button[@id='promtButton']", "Prompt box open button")
        self.__result_of_prompt_box = TextField("//span[@id='promptResult']", "Textfield with text from prompt box")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def open_alert_box(self):
        Logging.write_log_info("Open the simple alert box")
        self.__button_to_see_alert.click_on_the_element()

    def open_confirm_box(self):
        Logging.write_log_info("Open confirm alert box")
        self.__button_to_open_confirm_box.click_on_the_element()

    def get_the_text_from_confirm_box_label(self):
        Logging.write_log_info("Get text from confirm alert box label")
        return self.__result_of_confirm_box.get_text_from_element()

    def open_prompt_box(self):
        Logging.write_log_info("Open the prompt alert box")
        self.__button_to_open_prompt_box.click_on_the_element()

    def get_the_text_from_prompt_box_label(self):
        Logging.write_log_info("Get text from prompt alert box label")
        return self.__result_of_prompt_box.get_text_from_element()
