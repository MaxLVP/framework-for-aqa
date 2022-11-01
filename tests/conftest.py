import pytest
from browser_utils.singleton import Singleton
from utilsclasses.logger import Logging
from browser_utils.webdriver_factory import WebdriverFactory
from browser_utils.driver_utils import DriverUtils


@pytest.fixture(scope='function')
def working_driver():
    WebdriverFactory.set_up_webdriver()
    driver = Singleton.get_instance().driver
    Logging.write_log_info(f"Open Main page")
    DriverUtils().navigate_to_url()
    DriverUtils().maximize_window()
    yield
    driver.close()
    DriverUtils.clear_driver_instance()
