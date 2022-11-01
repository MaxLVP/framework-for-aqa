from pages.main_page import MainPage
from pages.alerts_windows_page import AlertsWindowsPage
from pages.browser_windows_page import BrowserWindows
from pages.links_page import Links


class TestHandles:

    def test_opening_and_closing_tabs(self, working_driver):
        main = MainPage()
        alert_frame_window = AlertsWindowsPage()
        window = BrowserWindows()
        links = Links()
        assert main.is_page_open(), f"{main.get_the_page_name()} page is not open"
        main.open_the_alerts_frames_windows_page()
        assert alert_frame_window.is_page_open(), f"{alert_frame_window.get_the_page_name()} page is not open"
        alert_frame_window.click_the_browser_windows_btn()
        assert window.is_page_open(), f"{window.get_the_page_name()} page is not open"
        assert window.open_new_tab(), "Tab is not open"
        assert window.is_page_open(), f"{window.get_the_page_name()} page is not open"
        window.open_links_page()
        assert links.is_page_open(), f"{links.get_the_page_name()} page is not open"
        links.open_the_home_page()
        assert main.is_page_open(), f"{main.get_the_page_name()} page is not open"
        links.resume_to_previous_tab()
        assert links.is_page_open(), f"{links.get_the_page_name()} page is not open"
