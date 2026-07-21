import random
import string

import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    SUPPLIER_NAMES,
    PAYMENT_TERMS,
    SUPPLIER_RATING
)
from utils.common import CommonUtils


class SupplierGenerator:

    def __init__(self):

        random.seed(RANDOM_SEED)

    ##################################################

    def generate_supplier_name(self):

        name = random.choice(SUPPLIER_NAMES)

        if random.random() < DIRTY_DATA["supplier"]["leading_spaces"]:

            name = CommonUtils.add_spaces(name)

        return name

    ##################################################

    def generate_gst_number(self):

        gst = (
            str(random.randint(10, 38)).zfill(2)
            + "".join(random.choices(string.ascii_uppercase, k=5))
            + "".join(random.choices(string.digits, k=4))
            + random.choice(string.ascii_uppercase)
            + "1Z"
            + random.choice(string.ascii_uppercase)
        )

        if random.random() < DIRTY_DATA["supplier"]["missing_gst"]:

            return None

        return gst

    ##################################################

    def generate_email(self, supplier_name):

        email = (
            supplier_name.lower()
            .replace(" ", "")
            .replace(".", "")
            + "@supplier.com"
        )

        return email

    ##################################################

    def generate_phone(self):

        return CommonUtils.random_phone()

    ##################################################

    def generate(self):

        rows = []

        supplier_id = SUPPLIER_ID_START

        for _ in range(TOTAL_SUPPLIERS):

            state, city = CommonUtils.choose_state_city()

            if random.random() < DIRTY_DATA["supplier"]["invalid_city"]:

                city = random.choice(

                    [
                        "Bombay",
                        "Bangalore City",
                        "Unknown",
                        "N/A"
                    ]

                )

            supplier_name = self.generate_supplier_name()

            rows.append(
                {

                    "Supplier ID": supplier_id,

                    "Supplier Name": supplier_name,

                    "GST Number": self.generate_gst_number(),

                    "Contact Email": self.generate_email(
                        supplier_name.strip()
                    ),

                    "Phone Number": self.generate_phone(),

                    "City": city,

                    "State": state,

                    "Country": "India",

                    "Payment Terms": random.choice(
                        PAYMENT_TERMS
                    ),

                    "Supplier Rating": random.choice(
                        SUPPLIER_RATING
                    )

                }

            )


            supplier_id += 1

        ##################################################
        # Duplicate Supplier Names
        ##################################################

        duplicate_count = CommonUtils.apply_percentage(

            TOTAL_SUPPLIERS,

            DIRTY_DATA["supplier"]["duplicate_supplier"]

        )

        duplicate_indexes = random.sample(

            list(range(1, TOTAL_SUPPLIERS)),

            duplicate_count

        )

        for idx in duplicate_indexes:

            rows[idx]["Supplier Name"] = rows[0]["Supplier Name"]

        ##################################################

        df = pd.DataFrame(rows)

        return df