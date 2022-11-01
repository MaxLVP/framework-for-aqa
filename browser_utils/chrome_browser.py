from selenium import webdriver
from selenium.webdriver import ChromeOptions
from browser_utils.singleton import Singleton
from utilsclasses.config_manager import WorkingWithData
from webdriver_manager.chrome import ChromeDriverManager
import os


class ChromeBrowser(metaclass=Singleton):

    def __init__(self):
        abs_path = os.path.abspath(__file__)
        file_directory = os.path.dirname(abs_path)
        project_directory = os.path.dirname(file_directory)
        download_filepath = os.path.join(project_directory, 'downloaded_files')
        prefs = {"download.default_directory": download_filepath}
        options = ChromeOptions()
        options.add_experimental_option("prefs", prefs)
        options.add_argument(WorkingWithData.working_with_data("incognito", "config"))
        options.add_argument(WorkingWithData.working_with_data("lang", "config"))
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
