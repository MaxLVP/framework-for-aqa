from base_class.base_form import BaseForm
from elements.textfield import TextField
from elements.button import Button
from browser_utils.singleton import Singleton
from utilsclasses.frames import Frames
from browser_utils.driver_utils import DriverUtils
from utilsclasses.logger import Logging


class NestedFramesPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Nested Frames"
        self.__header_of_page = TextField("//div[contains(text(), 'Nested') and contains(@class, 'main-header')]",
                                     "Header of Nested Frames page")
        self.__frames_page_open_btn = Button("//span[text() = 'Frames']", "Frames page open button")
        self.__parent_frame = Frames("//iframe[@id='frame1']", "Parent frame")
        self.__child_frame = Frames("//iframe[contains(@srcdoc, 'Child')]", "Child frame")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def get_the_text_from_frames(self):
        Logging.write_log_info("Searching for texts from Nested Frame page")
        self.__parent_frame.switch_to_frame()
        Logging.write_log_info(f"Getting text from parent frame on the {self.__name_of_the_page} ")
        parent_text = Singleton.get_instance().driver.find_element_by_tag_name("body").text
        self.__child_frame.switch_to_frame()
        Logging.write_log_info(f"Getting text from child frame on the {self.__name_of_the_page} ")
        child_text = Singleton.get_instance().driver.find_element_by_tag_name("p").text
        Logging.write_log_info("Switching to default frame")
        Singleton.get_instance().driver.switch_to.default_content()
        return child_text, parent_text

    def click_the_frames_page_btn(self):
        Logging.write_log_info("Open the Frames page")
        target = self.__frames_page_open_btn.find_element()
        DriverUtils().execute_js_script_to_scroll(target)
        self.__frames_page_open_btn.click_on_the_element()
