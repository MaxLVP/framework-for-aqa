from base_class.base_form import BaseForm
from elements.input import Input
from elements.button import Button
from elements.textfield import TextField
from utilsclasses.logger import Logging
from browser_utils.singleton import Singleton
from utilsclasses.config_manager import WorkingWithData
from utilclasses_for_tests.working_with_date import DateAndTime
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class DatePickerPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Date Picker"
        self.__header_of_page = TextField("//div[contains(text(), 'Picker') and contains(@class, 'main-header')]",
                                     "Header of Date Picker page")
        self.__select_date = Input("//input[@id='datePickerMonthYearInput']", "Select date input")
        self.__input_with_current_date_and_time = Input("//input[@id='dateAndTimePickerInput']", "Input_with_current_date_and_time")
        self.__select_month = Input("//select[contains(@class, 'month-select')]", "Select month")
        self.__select_year = Input("//select[contains(@class, 'year-select')]", "Select year")
        self.day = WorkingWithData.working_with_data("day_to_set", "test")
        self.month = WorkingWithData.working_with_data("month_to_set", "test")
        self.month_number = WorkingWithData.working_with_data("number_of_month_to_set", "test")
        self.year = WorkingWithData.working_with_data("year_to_set", "test")
        self.__select_day = Button(f"//div[contains(@aria-label, '{self.month} {self.day}')]", "Select day button")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def get_the_current_date_and_time(self):
        Logging.write_log_info("Getting the date and time from Date Picker page")
        current_time = self.__input_with_current_date_and_time.get_the_attribute_value("value")
        return current_time

    def set_the_date(self):
        Logging.write_log_info(f"Set the date to date input")
        if self.year == "leap":
            self.year = DateAndTime.get_the_nearest_leap_year()
        self.__select_date.click_on_the_element()
        select_month_element = self.__select_month.find_element()
        select_month = Select(select_month_element)
        Logging.write_log_info(f"Select {self.month} month")
        select_month.select_by_visible_text(self.month)
        select_year_element = self.__select_year.find_element()
        select_year = Select(select_year_element)
        Logging.write_log_info(f"Select {self.year} year")
        select_year.select_by_visible_text(self.year)
        Logging.write_log_info(f"Select {self.day} day")
        self.__select_day.click_on_the_element()
        waits = WebDriverWait(Singleton.get_instance().driver, DatePickerPage.waits).until(ec.text_to_be_present_in_element_attribute((By.XPATH, self.__select_date.locator), "value", self.year))

    def get_the_valid_data(self):
        Logging.write_log_info("Get the valid date")
        valid_data = f"{self.month_number}/{self.day}/{self.year}"
        return valid_data

    def get_the_value_of_set_date(self):
        Logging.write_log_info("Get the actual date that sets in input")
        set_date = self.__select_date.get_the_attribute_value("value")
        return set_date






