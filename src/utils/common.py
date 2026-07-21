import random
import string
from datetime import datetime, timedelta

from configs.master_data import STATE_CITY


class CommonUtils:

    @staticmethod
    def random_date(
            start_date,
            end_date
    ):

        if isinstance(start_date, str):

            start_date = datetime.strptime(
                start_date,
                "%Y-%m-%d"
            )

        if isinstance(end_date, str):

            end_date = datetime.strptime(
                end_date,
                "%Y-%m-%d"
            )

        days = (
            end_date - start_date
        ).days

        return start_date + timedelta(
            days=random.randint(
                0,
                days
            )
        )

    ##################################################

    @staticmethod
    def random_future_date():

        return datetime(
            random.randint(2027, 2029),
            random.randint(1, 12),
            random.randint(1, 28)
        )

    ##################################################

    @staticmethod
    def format_date(date):

        if isinstance(date, str):

            return date

        return date.strftime(
            "%Y-%m-%d"
        )

    ##################################################

    @staticmethod
    def random_phone():

        number = "9"

        number += "".join(
            random.choice(string.digits)
            for _ in range(9)
        )

        option = random.randint(1, 4)

        if option == 1:

            return number

        elif option == 2:

            return "+91 " + number

        elif option == 3:

            return (
                number[:5]
                + "-"
                + number[5:]
            )

        else:

            return (
                number[:3]
                + " "
                + number[3:6]
                + " "
                + number[6:]
            )

    ##################################################

    @staticmethod
    def random_email(
            first_name,
            last_name
    ):

        domains = [
            "gmail.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com"
        ]

        first = first_name.strip().lower()

        last = last_name.strip().lower()

        return (
            first
            + "."
            + last
            + "@"
            + random.choice(domains)
        )

    ##################################################

    @staticmethod
    def random_case(text):

        option = random.randint(1, 4)

        if option == 1:

            return text.upper()

        elif option == 2:

            return text.lower()

        elif option == 3:

            return text.title()

        return text

    ##################################################

    @staticmethod
    def add_spaces(text):

        option = random.randint(1, 4)

        if option == 1:

            return " " + text

        elif option == 2:

            return text + " "

        elif option == 3:

            return " " + text + " "

        return text

    ##################################################

    @staticmethod
    def random_price(
            min_price,
            max_price
    ):

        return round(
            random.uniform(
                min_price,
                max_price
            ),
            2
        )

    ##################################################

    @staticmethod
    def choose_state_city():

        state = random.choice(
            list(STATE_CITY.keys())
        )

        city = random.choice(
            STATE_CITY[state]
        )

        return (
            state,
            city
        )

    ##################################################

    @staticmethod
    def apply_percentage(
            total_rows,
            percentage
    ):

        return int(
            total_rows * percentage
        )

    ##################################################

    @staticmethod
    def random_sku(category):

        prefix = "".join(
            word[0].upper()
            for word in category.split()
        )

        suffix = "".join(
            random.choices(
                string.ascii_uppercase
                + string.digits,
                k=6
            )
        )

        return f"{prefix}-{suffix}"

    ##################################################

    @staticmethod
    def random_name():

        return "".join(
            random.choices(
                string.ascii_uppercase,
                k=5
            )
        )

    ##################################################

    @staticmethod
    def calculate_percentage(
            value,
            percentage
    ):

        return round(
            value * percentage / 100,
            2
        )

    ##################################################

    @staticmethod
    def round_currency(value):

        return round(
            value,
            2
        )