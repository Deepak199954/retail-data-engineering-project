
import random

import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    STATE_CITY,
    STORE_NAMES,
    STORE_TYPES,
    REGIONS,
    STORE_STATUS
)

from utils.common import CommonUtils


class StoreGenerator:
    """
    Generates enterprise-grade Store Master data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # STORE NAME
    # ==========================================================

    def generate_store_name(
            self,
            city
    ):

        prefix = random.choice(
            STORE_NAMES
        )

        return f"{prefix} {city}"

    # ==========================================================
    # ADDRESS
    # ==========================================================

    def generate_address(self):

        building = random.randint(
            1,
            999
        )

        roads = [

            "MG Road",
            "Station Road",
            "Park Street",
            "Commercial Street",
            "Main Road",
            "Ring Road",
            "Market Road",
            "High Street",
            "Airport Road",
            "Lake View Road"

        ]

        return f"{building}, {random.choice(roads)}"

    # ==========================================================
    # POSTAL CODE
    # ==========================================================

    def generate_postal_code(self):

        return random.randint(
            100000,
            999999
        )

    # ==========================================================
    # STORE EMAIL
    # ==========================================================

    def generate_email(
            self,
            city
    ):

        value = city.lower().replace(
            " ",
            ""
        )

        return f"{value}@retailmart.com"

    # ==========================================================
    # OPENING DATE
    # ==========================================================

    def generate_opening_date(self):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                "2015-01-01",
                "2025-12-31"
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

            record["City"] = CommonUtils.random_case(
                record["City"]
            )

        if random.random() < 0.02:

            record["State"] = CommonUtils.random_case(
                record["State"]
            )

        if random.random() < 0.02:

            record["Address"] = CommonUtils.add_spaces(
                record["Address"]
            )

        if random.random() < 0.01:

            record["Email"] = "invalid-email"

        if random.random() < 0.01:

            record["Phone"] = "99999"

        if random.random() < 0.01:

            record["Opening Date"] = (
                CommonUtils.format_date(
                    CommonUtils.random_future_date()
                )
            )

        return record
	# ==========================================================
    # GENERATE STORE MASTER
    # ==========================================================

    def generate(self):

        rows = []

        store_id = STORE_ID_START

        for _ in range(TOTAL_STORES):

            state = random.choice(
                list(STATE_CITY.keys())
            )

            city = random.choice(
                STATE_CITY[state]
            )

            opening_date = self.generate_opening_date()

            record = {

                "Store ID": CommonUtils.generate_id(
                    "STR",
                    store_id,
                    5
                ),

                "Store Name": self.generate_store_name(
                    city
                ),

                "Store Type": random.choice(
                    STORE_TYPES
                ),

                "Region": REGIONS[
                    state
                ],

                "State": state,

                "City": city,

                "Address": self.generate_address(),

                "Postal Code": self.generate_postal_code(),

                "Phone": CommonUtils.random_phone(),

                "Email": self.generate_email(
                    city
                ),

                "Manager ID": None,

                "Opening Date": opening_date,

                "Store Status": random.choice(
                    STORE_STATUS
                )

            }

            record["Created Date"] = opening_date

            record["Updated Date"] = CommonUtils.format_date(
                CommonUtils.random_date(
                    opening_date,
                    "2026-06-30"
                )
            )

            record = self.apply_dirty_data(
                record
            )

            rows.append(
                record
            )

            store_id += 1

        return pd.DataFrame(
            rows
        )