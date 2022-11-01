from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from browser_utils.singleton import Singleton
from utilsclasses.config_manager import WorkingWithData
from webdriver_manager.firefox import GeckoDriverManager
import os


class FirefoxBrowser(metaclass=Singleton):

    def __init__(self):
        abs_path = os.path.abspath(__file__)
        file_directory = os.path.dirname(abs_path)
        project_directory = os.path.dirname(file_directory)
        download_filepath = os.path.join(project_directory, 'downloaded_files')
        options = FirefoxOptions()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", download_filepath)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
        if WorkingWithData.working_with_data("incognito", "config") == "true":
            options.add_argument("-private")
        options.add_argument(WorkingWithData.working_with_data("lang", "config"))
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
