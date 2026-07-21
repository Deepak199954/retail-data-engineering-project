import random

import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    STATE_CITY,
    CUSTOMER_TYPES,
    CUSTOMER_STATUS
)
from utils.common import CommonUtils


class CustomerGenerator:

    def __init__(self):

        random.seed(RANDOM_SEED)

        self.first_names = [

            "Rahul",
            "Amit",
            "Rohit",
            "Neha",
            "Priya",
            "Sneha",
            "Anjali",
            "Karan",
            "Vikram",
            "Pooja",
            "Deepak",
            "Suresh",
            "Mahesh",
            "Arjun",
            "Riya",
            "Divya",
            "Nikhil",
            "Aditya",
            "Shreya",
            "Akash"

        ]

        self.last_names = [

            "Sharma",
            "Patel",
            "Singh",
            "Verma",
            "Gupta",
            "Joshi",
            "Kulkarni",
            "Reddy",
            "Nair",
            "Jain"

        ]

    ####################################################

    def random_signup_date(self):

        signup_date = CommonUtils.random_date(
            DATA_START_DATE,
            DATA_END_DATE
        )

        if random.random() < DIRTY_DATA["customer"]["future_signup_date"]:

            signup_date = CommonUtils.random_future_date()

        return signup_date

    ####################################################

    def generate_email(self, first_name, last_name):

        email = CommonUtils.random_email(
            first_name,
            last_name
        )

        if random.random() < DIRTY_DATA["customer"]["uppercase_email"]:

            email = email.upper()

        if random.random() < DIRTY_DATA["customer"]["invalid_email"]:

            email = email.replace("@", "")

        return email

    ####################################################

    def generate_phone(self):

        return CommonUtils.random_phone()

    ####################################################

    def dirty_name(self, name):

        if random.random() < DIRTY_DATA["customer"]["leading_trailing_spaces"]:

            name = CommonUtils.add_spaces(name)

        if random.random() < DIRTY_DATA["customer"]["mixed_case"]:

            name = CommonUtils.random_case(name)

        return name

    ####################################################

    def generate(self):

        rows = []

        customer_id = CUSTOMER_ID_START

        for _ in range(TOTAL_CUSTOMERS):

            first_name = random.choice(
                self.first_names
            )

            last_name = random.choice(
                self.last_names
            )

            customer_name = self.dirty_name(
                first_name + " " + last_name
            )

            state, city = CommonUtils.choose_state_city()

            if random.random() < DIRTY_DATA["customer"]["null_city"]:

                city = None

            signup_date = self.random_signup_date()

            email = self.generate_email(
                first_name,
                last_name
            )

            phone = self.generate_phone()

            customer_type = random.choice(
                CUSTOMER_TYPES
            )

            if random.random() < DIRTY_DATA["customer"]["invalid_customer_type"]:

                customer_type = random.choice(

                    [

                        "Reg",
                        "REGULAR",
                        "Premium Customer",
                        "Gold Plus",
                        "VIP+"

                    ]

                )

            loyalty_points = random.randint(
                0,
                10000
            )

            if random.random() < DIRTY_DATA["customer"]["negative_loyalty_points"]:

                loyalty_points = -100

            customer_status = random.choice(
                CUSTOMER_STATUS
            )

            rows.append(

                {

                    "Customer ID": customer_id,

                    "Customer Name": customer_name,

                    "Email Address": email,

                    "Phone Number": phone,

                    "City": city,

                    "State": state,

                    "Country": "India",

                    "Signup Date": CommonUtils.format_date(
                        signup_date
                    ),

                    "Customer Type": customer_type,

                    "Customer Status": customer_status,

                    "Loyalty Points": loyalty_points

                }

            )

            customer_id += 1

        df = pd.DataFrame(rows)

        ####################################################
        # Duplicate Email
        ####################################################
        
        duplicate_count = CommonUtils.apply_percentage(

            TOTAL_CUSTOMERS,

            DIRTY_DATA["customer"]["duplicate_email"]

        )

        indexes = random.sample(

            list(df.index),

            duplicate_count

        )

        for idx in indexes:

            df.loc[idx, "Email Address"] = df.loc[
                0,
                "Email Address"
            ]

        ####################################################
        # Duplicate Phone
        ####################################################

        duplicate_count = CommonUtils.apply_percentage(

            TOTAL_CUSTOMERS,

            DIRTY_DATA["customer"]["duplicate_phone"]

        )

        indexes = random.sample(

            list(df.index),

            duplicate_count

        )

        for idx in indexes:

            df.loc[idx, "Phone Number"] = df.loc[
                1,
                "Phone Number"
            ]

        ####################################################

        return df