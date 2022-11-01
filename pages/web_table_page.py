from base_class.base_form import BaseForm
from elements.button import Button
from elements.textfield import TextField
from elements.input import Input
from utilsclasses.logger import Logging
from browser_utils.singleton import Singleton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class WebTablesPage(BaseForm):

    def __init__(self):
        self.__name_of_the_page = "Web Tables"
        self.__header_of_page = TextField("//div[contains(text(), 'Web Tables') and contains(@class, 'main-header')]",
                                     "Header of Web tables page")
        self.__add_new_entries_to_table_btn = Button("//button[@id='addNewRecordButton']", "Add entries to table button")
        self.__registration_form_textfield = TextField("//div[@id='registration-form-modal']",
                                                  "Textfield of registration form")
        self.__registration_form_submit_btn = Button("//button[@id='submit']", "Submit button on registration form")
        self.__first_name_input = Input("//input[@id='firstName']", "First name input")
        self.__last_name_input = Input("//input[@id='lastName']", "Last name input")
        self.__email_input = Input("//input[@id='userEmail']", "Email input")
        self.__age_input = Input("//input[@id='age']", "Age input")
        self.__salary_input = Input("//input[@id='salary']", "Salary input")
        self.__department_input = Input("//input[@id='department']", "Department input")
        self.__delete_icons = Button("//span[contains(@id,'delete-record')]", "All delete icons button")
        super().__init__(self.__header_of_page, self.__name_of_the_page)

    def open_the_registration_form(self):
        Logging.write_log_info("Open registration form")
        self.__add_new_entries_to_table_btn.click_on_the_element()
        return self.__registration_form_textfield.find_element().is_displayed()

    def enter_the_values_to_the_form(self, first_name, last_name, email, age, salary, department):
        Logging.write_log_info("Insert values from file to form")
        WebTablesPage().enter_the_name(first_name)
        WebTablesPage().enter_the_surname(last_name)
        WebTablesPage().enter_the_email(email)
        WebTablesPage().enter_the_age(age)
        WebTablesPage().enter_the_salary(salary)
        WebTablesPage().enter_the_department(department)
        Logging.write_log_info("Close registration form")
        self.__registration_form_submit_btn.click_on_the_element()
        waits = WebDriverWait(Singleton.get_instance().driver, WebTablesPage.waits).until(
            ec.invisibility_of_element_located((By.XPATH, self.__first_name_input.locator)))

    def check_if_form_closed(self):
        Logging.write_log_info("Check if registration form closed")
        elms = self.__first_name_input.find_elements()
        if len(elms) > 0:
            return False
        else:
            return True

    def check_the_right_values_appeared(self, first_name, last_name, age, email, salary, department):
        Logging.write_log_info("Checking the appeared data")
        first_name = TextField(f"//div[text()='{first_name}']", "first_name_value").get_text_from_element()
        last_name = TextField(f"//div[text()='{last_name}']", "last_name_value").get_text_from_element()
        age = TextField(f"//div[text()='{age}']", "last_name_value").get_text_from_element()
        email = TextField(f"//div[text()='{email}']", "last_name_value").get_text_from_element()
        salary = TextField(f"//div[text()='{salary}']", "last_name_value").get_text_from_element()
        department = TextField(f"//div[text()='{department}']", "last_name_value").get_text_from_element()
        return first_name, last_name, age, email, salary, department

    def delete_the_entries_by_specific_value(self, email):

        Logging.write_log_info(f"Deleting entries with specific value {email}")
        delete_btn = Button(f"//div[text()='{email}']//following-sibling::div//div[@class='action-buttons']//span[contains(@id, 'delete-record')]", "delete_icon")
        delete_btn.click_on_the_element()

    def check_last_entries_deleted(self, email):

        """Checking only unique element to delete."""

        email_field = TextField(f"//div[text()='{email}']", "first_name_value")
        find_elements = email_field.find_elements()
        if len(find_elements) > 0:
            return False
        else:
            return True

    def enter_the_name(self, name):
        self.__first_name_input.send_value(name)

    def enter_the_surname(self, surname):
        self.__last_name_input.send_value(surname)

    def enter_the_email(self, email):
        self.__email_input.send_value(email)

    def enter_the_age(self, age):
        self.__age_input.send_value(age)

    def enter_the_salary(self, salary):
        self.__salary_input.send_value(salary)

    def enter_the_department(self, department):
        self.__department_input.send_value(department)

