import pytest
from utilsclasses.working_with_ddt import GetDataForDDT
from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.web_table_page import WebTablesPage


class TestTables:

    keys_and_values = GetDataForDDT.get_data_for_ddt()

    @pytest.mark.parametrize(keys_and_values[0], keys_and_values[1])
    def test_tables(self, working_driver, first_name, last_name, email, age, salary, department):
        test_data = (first_name, last_name, age, email, salary, department)
        main = MainPage()
        element = ElementsPage()
        web_table = WebTablesPage()
        assert main.is_page_open(), f"{main.get_the_page_name()} page is not open"
        main.open_the_elements_page()
        assert element.is_page_open(), f"{element.get_the_page_name()} page is not open"
        element.open_the_web_tables_page()
        assert web_table.is_page_open(), f"{web_table.get_the_page_name()} page is not open"
        assert web_table.open_the_registration_form(), "Registration form is not open"
        web_table.enter_the_values_to_the_form(first_name, last_name, email, age, salary, department)
        assert web_table.check_if_form_closed(), "Registration form is not closed"
        appeared_entries = web_table.check_the_right_values_appeared(first_name, last_name, age, email, salary, department)
        assert appeared_entries == test_data, "Values from file are not appeared"
        web_table.delete_the_entries_by_specific_value(email)
        assert web_table.check_last_entries_deleted(email), "Last Entries did not delete"
