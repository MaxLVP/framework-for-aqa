from base_class.base_form import BaseForm
from elements.textfield import TextField
from elements.button import Button
from elements.input import Input
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilclasses_for_tests.custom_waits import FileIsDownload
from utilsclasses.logger import Logging
from browser_utils.singleton import Singleton
import os


class UploadAndDownloadPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Upload and Download"
        self.__header_of_page = TextField("//div[contains(text(), 'Upload') and contains(@class, 'main-header')]",
                                     "Upload and Download page")
        self.__download_btn = Button("//a[@id='downloadButton']", "Download file button")
        self.__upload_btn = Input("//input[@id='uploadFile']", "Upload file button")
        self.__upload_filename = TextField("//p[@id='uploadedFilePath']", "Upload file name textfield")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def get_the_download_path(self):
        abs_path = os.path.abspath(__file__)
        file_directory = os.path.dirname(abs_path)
        project_directory = os.path.dirname(file_directory)
        download_filepath = os.path.join(project_directory,
                                         f'downloaded_files/{UploadAndDownloadPage.get_the_download_file_name(self)}')
        return download_filepath

    def get_the_download_file_name(self):
        filename = self.__download_btn.get_the_attribute_value("download")
        return filename

    def download_file(self):
        Logging.write_log_info(f"Downloading {self.get_the_download_file_name()} file")
        self.__download_btn.click_on_the_element()
        waits = WebDriverWait(Singleton.get_instance().driver, UploadAndDownloadPage.waits).until(FileIsDownload(UploadAndDownloadPage.get_the_download_path(self)))

    def upload_file(self):
        Logging.write_log_info(f"Waiting for downloading {self.get_the_download_file_name()} file")
        Logging.write_log_info(f"Uploading {self.get_the_download_file_name()} file")
        self.__upload_btn.send_value(UploadAndDownloadPage.get_the_download_path(self))
        waits = WebDriverWait(Singleton.get_instance().driver, UploadAndDownloadPage.waits).until(ec.element_to_be_clickable(self.__upload_filename.find_element()))
        return self.__upload_filename.element_is_displayed()
