import random

import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    DEPARTMENTS,
    DESIGNATIONS,
    EMPLOYMENT_TYPES,
    EMPLOYEE_STATUS
)

from utils.common import CommonUtils


class EmployeeGenerator:
    """
    Generates enterprise-grade Employee Master data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # EMPLOYEE NAME
    # ==========================================================

    def generate_employee_name(self):

        first_names = [

            "Rahul",
            "Amit",
            "Vikas",
            "Neha",
            "Pooja",
            "Sneha",
            "Priya",
            "Rohit",
            "Karan",
            "Arjun",
            "Anjali",
            "Nikita",
            "Deepak",
            "Suresh",
            "Ramesh",
            "Akash",
            "Ankit",
            "Meera",
            "Swati",
            "Komal"

        ]

        last_names = [

            "Sharma",
            "Patel",
            "Verma",
            "Singh",
            "Gupta",
            "Jain",
            "Joshi",
            "Nair",
            "Kulkarni",
            "Yadav",
            "Reddy",
            "Iyer",
            "Das",
            "Chauhan",
            "Mishra"

        ]

        return (

            random.choice(first_names),

            random.choice(last_names)

        )

    # ==========================================================
    # DATE OF BIRTH
    # ==========================================================

    def generate_dob(self):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                "1980-01-01",
                "2004-12-31"
            )
        )

    # ==========================================================
    # EMAIL
    # ==========================================================

    def generate_email(
            self,
            first_name,
            last_name
    ):

        email = (

            first_name.lower()

            + "."

            + last_name.lower()

            + "@retailmart.com"

        )

        return email

    # ==========================================================
    # SALARY
    # ==========================================================

    def generate_salary(
            self,
            designation
    ):

        salary_range = {

            "Store Manager": (70000, 120000),

            "Assistant Manager": (50000, 80000),

            "Sales Executive": (25000, 45000),

            "Cashier": (22000, 35000),

            "Inventory Executive": (30000, 50000),

            "Warehouse Associate": (22000, 35000),

            "HR Executive": (35000, 60000),

            "Finance Executive": (40000, 65000),

            "IT Support": (45000, 75000)

        }

        minimum, maximum = salary_range.get(

            designation,

            (25000, 45000)

        )

        return random.randint(

            minimum,

            maximum

        )

    # ==========================================================
    # HIRE DATE
    # ==========================================================

    def generate_hire_date(self):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                "2016-01-01",
                "2026-06-30"
            )
        )

    # ==========================================================
    # DIRTY DATA
    # ==========================================================

    def apply_dirty_data(
            self,
            record
    ):

        if random.random() < 0.02:

            record["First Name"] = CommonUtils.random_case(

                record["First Name"]

            )

        if random.random() < 0.02:

            record["Last Name"] = CommonUtils.add_spaces(

                record["Last Name"]

            )

        if random.random() < 0.01:

            record["Email"] = "invalid-email"

        if random.random() < 0.01:

            record["Phone"] = None

        if random.random() < 0.01:

            record["Salary"] = -record["Salary"]

        if random.random() < 0.01:

            record["Hire Date"] = (
                CommonUtils.format_date(
                    CommonUtils.random_future_date()
                )
            )

        if random.random() < 0.01:

            record["Employment Type"] = "Temporary Worker"

        return record
	# ==========================================================
    # GENERATE EMPLOYEE MASTER
    # ==========================================================

    def generate(
        self,
        stores_df
    ):

        rows = []

        employee_id = EMPLOYEE_ID_START

        for _ in range(TOTAL_EMPLOYEES):

            first_name, last_name = self.generate_employee_name()

            designation = random.choice(
                DESIGNATIONS
            )

            hire_date = self.generate_hire_date()

            record = {

                "Employee ID": CommonUtils.generate_id(
                    "EMP",
                    employee_id,
                    5
                ),

                "First Name": first_name,

                "Last Name": last_name,

                "Gender": random.choice(
                    [
                        "Male",
                        "Female"
                    ]
                ),

                "DOB": self.generate_dob(),

                "Email": self.generate_email(
                    first_name,
                    last_name
                ),

                "Phone": CommonUtils.random_phone(),

                "Store ID": random.choice(
                    stores_df["Store ID"].tolist()
                ),

                "Department": random.choice(
                    DEPARTMENTS
                ),

                "Designation": designation,

                "Hire Date": hire_date,

                "Salary": self.generate_salary(
                    designation
                ),

                "Employment Type": random.choice(
                    EMPLOYMENT_TYPES
                ),

                "Employee Status": random.choice(
                    EMPLOYEE_STATUS
                ),

                "Manager Employee ID": None

            }

            record["Created Date"] = hire_date

            record["Updated Date"] = CommonUtils.format_date(
                CommonUtils.random_date(
                    hire_date,
                    "2026-06-30"
                )
            )

            record = self.apply_dirty_data(
                record
            )

            rows.append(
                record
            )

            employee_id += 1

        return pd.DataFrame(
            rows
        )