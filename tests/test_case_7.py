from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.upload_and_download_page import UploadAndDownloadPage


class TestFiles:

    def test_files(self, working_driver):
        main = MainPage()
        element = ElementsPage()
        upload = UploadAndDownloadPage()
        assert main.is_page_open(), f"{main.get_the_page_name()} page is not open"
        main.open_the_elements_page()
        assert element.is_page_open(), f"{element.get_the_page_name()} page is not open"
        element.open_the_upload_and_download_page()
        assert upload.is_page_open(), f"{upload.get_the_page_name()} page is not open"
        downloaded_filename = upload.get_the_download_file_name()
        upload.download_file()
        assert upload.upload_file(), f"{downloaded_filename} file is not uploaded"
