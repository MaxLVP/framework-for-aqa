from utilsclasses.logger import Logging
from pages.main_page import MainPage
from pages.widgets_page import WidgetsPage
from pages.date_picker_page import DatePickerPage
from utilclasses_for_tests.working_with_date import DateAndTime


class TestDataPicker:

    def test_pick_the_nearest_date(self, working_driver):
        main = MainPage()
        widgets = WidgetsPage()
        date_picker = DatePickerPage()
        assert main.is_page_open(), f"{main.get_the_page_name()} is not open"
        main.open_the_widgets_page()
        assert widgets.is_page_open(), f"{widgets.get_the_page_name()} is not open"
        widgets.open_the_data_picker_page()
        assert date_picker.is_page_open(), f"{date_picker.get_the_page_name()} is not open"
        time_from_page = date_picker.get_the_current_date_and_time()
        Logging.write_log_info("Getting current time")
        current_time = DateAndTime.get_the_current_date_and_time()
        Logging.write_log_info("Comparing time from page with current time")
        assert time_from_page == current_time, f"{time_from_page} is not match with {current_time}"
        date_picker.set_the_date()
        set_date = date_picker.get_the_value_of_set_date()
        valid_date = date_picker.get_the_valid_data()
        assert set_date == valid_date, f"Set date {set_date} does not math to valid date {valid_date}"


