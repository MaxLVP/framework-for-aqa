from utilsclasses.logger import Logging
from utilsclasses.config_manager import WorkingWithData
from utilclasses_for_tests.generate_values import GenerateRandomValue
from utilsclasses.working_with_alerts import Alerts
from pages.main_page import MainPage
from pages.alerts_windows_page import AlertsWindowsPage
from pages.alerts_page import AlertsPage


class TestAlerts:

    def test_different_alerts_boxes(self, working_driver):
        length = 5
        main = MainPage()
        alert_win = AlertsWindowsPage()
        alert_page = AlertsPage()
        assert main.is_page_open(), f"{main.get_the_page_name()} is not open"
        main.open_the_alerts_frames_windows_page()
        assert alert_win.is_page_open(), f"{alert_win.get_the_page_name()} page is not open"
        alert_win.click_the_alerts_btn()
        assert alert_page.is_page_open(), f"{alert_page.get_the_page_name()} page is not open"
        alert_page.open_alert_box()
        alerts = Alerts()
        alert_text = alerts.get_the_text_from_alert()
        text_to_compare = WorkingWithData.working_with_data("text_on_the_alert_box", 'test')
        Logging.write_log_info("Comparing text from alert box")
        assert alert_text == text_to_compare, f"Alert with text {text_to_compare} is not open"
        alerts.click_the_accept()
        assert Alerts.check_alert_box_is_closed(), "Alert box is not closed"
        alert_page.open_confirm_box()
        alerts = Alerts()
        alert_text = alerts.get_the_text_from_alert()
        text_to_compare = WorkingWithData.working_with_data("text_on_the_confirm_box", 'test')
        Logging.write_log_info("Comparing text from alert box")
        assert alert_text == text_to_compare, f"Alert with text {text_to_compare} is not open"
        alerts.click_the_accept()
        assert Alerts.check_alert_box_is_closed(), "Alert box is not closed"
        appeared_text_after_confirm_box = alert_page.get_the_text_from_confirm_box_label()
        text_after_confirm_box = WorkingWithData.working_with_data("result_after_confirm_box", "test")
        Logging.write_log_info("Comparing appeared text from confirm box")
        assert text_after_confirm_box in appeared_text_after_confirm_box, f"Text {text_after_confirm_box} on confirm box label is not appeared"
        alert_page.open_prompt_box()
        text_to_send_prompt_box = GenerateRandomValue.generate_text(length)
        alerts = Alerts()
        alert_text = alerts.get_the_text_from_alert()
        text_to_compare = WorkingWithData.working_with_data("text_on_the_prompt_box", 'test')
        Logging.write_log_info("Comparing text from alert box")
        assert alert_text == text_to_compare, f"Alert with text {text_to_compare} is not open"
        alerts.send_keys_and_accept(text_to_send_prompt_box)
        text_appeared_after_prompt_box = alert_page.get_the_text_from_prompt_box_label()
        assert Alerts.check_alert_box_is_closed(), "Alert box is not closed"
        Logging.write_log_info("Comparing appeared text from prompt box")
        assert text_to_send_prompt_box in text_appeared_after_prompt_box, f"Text does not match with {text_to_send_prompt_box}"
