from pages import main_page
from pages import nested_frames_page
from pages import frame_page
from pages import alerts_windows_page
from utilsclasses.logger import Logging
from utilsclasses.config_manager import WorkingWithData


class TestIframe:

    def test_switching_between_frames(self, working_driver):
        main = main_page.MainPage()
        alert_frame = alerts_windows_page.AlertsWindowsPage()
        nested_frame = nested_frames_page.NestedFramesPage()
        frame = frame_page.FramesPage()
        child, first = 0, 0
        parent, second = 1, 1
        assert main.is_page_open(), f"{main.get_the_page_name()} page is not open"
        main.open_the_alerts_frames_windows_page()
        assert alert_frame.is_page_open(), f"{alert_frame.get_the_page_name()} page is not open"
        alert_frame.click_the_nested_frames_btn()
        assert nested_frame.is_page_open(), f"{nested_frame.get_the_page_name()} page is not open"
        child_text = WorkingWithData.working_with_data("text_in_child_frame", "test")
        parent_text = WorkingWithData.working_with_data("text_in_parent_frame", "test")
        nested_frames_texts = nested_frame.get_the_text_from_frames()
        Logging.write_log_info(f"Comparing text on page with {child_text}")
        assert nested_frames_texts[child] == child_text, "Text are not on the page"
        Logging.write_log_info(f"Comparing text on page with {parent_text}")
        assert nested_frames_texts[parent] == parent_text, "Text are not on the page"
        nested_frame.click_the_frames_page_btn()
        assert frame.is_page_open(), f"{frame.get_the_page_name()} page is not open"
        texts = frame.check_the_text_from_frames()
        Logging.write_log_info("Comparing texts from frames")
        assert texts[first] == texts[second], "Text are not the same"
