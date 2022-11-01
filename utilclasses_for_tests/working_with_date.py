from datetime import datetime


class DateAndTime:

    @staticmethod
    def get_the_current_date_and_time():
        now = datetime.now()
        dat_string = now.strftime("%B %#d, %Y %#I:%M %p")
        return dat_string

    @staticmethod
    def get_the_nearest_leap_year():
        year = datetime.now().year
        while True:
            if year % 4 == 0 and (year % 100 != 0 and year % 400 != 0):
                break
            year += 1
        return str(year)
