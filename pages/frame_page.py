from base_class.base_form import BaseForm
from elements.textfield import TextField
from utilsclasses.frames import Frames
from browser_utils.singleton import Singleton
from utilsclasses.logger import Logging


class FramesPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Frames"
        self.__header_of_page = TextField("//div[contains(text(), 'Frames') and contains(@class, 'main-header')]",
                                     "Header of Frames page")
        self.__first_frame = Frames("//iframe[@id='frame1']", "First frame")
        self.__second_frame = Frames("//iframe[@id='frame2']", "Second frame")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def check_the_text_from_frames(self):
        self.__first_frame.switch_to_frame()
        Logging.write_log_info(f"Getting text from first frame on the {self.__name_of_the_page}")
        first_frame_text = Singleton.get_instance().driver.find_element_by_tag_name("h1").text
        Singleton.get_instance().driver.switch_to.default_content()
        self.__second_frame.switch_to_frame()
        Logging.write_log_info(f"Getting text from second frame on the {self.__name_of_the_page}")
        second_frame_text = Singleton.get_instance().driver.find_element_by_tag_name("h1").text
        return first_frame_text, second_frame_text
