from utilsclasses.config_manager import WorkingWithData
from browser_utils.chrome_browser import ChromeBrowser
from browser_utils.firefox_browser import FirefoxBrowser


class WebdriverFactory:

    CHROME = 'chrome'
    FIREFOX = 'firefox'

    @staticmethod
    def set_up_webdriver():
        browser_name = WorkingWithData.working_with_data("browser", "config")
        if browser_name == WebdriverFactory.FIREFOX:
            browser = FirefoxBrowser()
        elif browser_name == WebdriverFactory.CHROME:
            browser = ChromeBrowser()
        else:
            browser = ChromeBrowser()
