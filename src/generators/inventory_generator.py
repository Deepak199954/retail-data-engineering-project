

import random

import pandas as pd

from configs.dataset_config import *

from utils.common import CommonUtils


class InventoryGenerator:
    """
    Generates enterprise-grade Inventory data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # QUANTITY
    # ==========================================================

    def generate_quantity(self):

        return random.randint(
            0,
            500
        )

    # ==========================================================
    # REORDER LEVEL
    # ==========================================================

    def generate_reorder_level(self):

        return random.randint(
            20,
            100
        )

    # ==========================================================
    # MAXIMUM STOCK
    # ==========================================================

    def generate_maximum_stock(
            self,
            reorder_level
    ):

        return random.randint(
            reorder_level + 50,
            reorder_level + 500
        )

    # ==========================================================
    # INVENTORY STATUS
    # ==========================================================

    def generate_inventory_status(
            self,
            quantity,
            reorder_level
    ):

        if quantity == 0:

            return "OUT OF STOCK"

        elif quantity <= reorder_level:

            return "LOW STOCK"

        return "IN STOCK"

    # ==========================================================
    # LAST RESTOCKED DATE
    # ==========================================================

    def generate_last_restocked_date(self):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                "2024-01-01",
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

        if random.random() < 0.01:

            record["Quantity Available"] = (
                -record["Quantity Available"]
            )

        if random.random() < 0.01:

            record["Quantity Available"] = (
                record["Maximum Stock"] + 100
            )

        if random.random() < 0.01:

            record["Unit Cost"] = (
                -record["Unit Cost"]
            )

        if random.random() < 0.01:

            record["Inventory Status"] = (
                CommonUtils.random_case(
                    record["Inventory Status"]
                )
            )

        if random.random() < 0.01:

            record["Inventory Status"] = (
                "AVAILABLE"
            )

        if random.random() < 0.01:

            record["Unit Cost"] = None

        if random.random() < 0.01:

            record["Last Restocked Date"] = (
                CommonUtils.format_date(
                    CommonUtils.random_future_date()
                )
            )

        return record
	# ==========================================================
    # GENERATE INVENTORY
    # ==========================================================

    def generate(
            self,
            stores_df,
            products_df
    ):

        rows = []

        inventory_id = INVENTORY_ID_START

        for _, product in products_df.iterrows():

            for _, store in stores_df.iterrows():

                quantity = self.generate_quantity()

                reorder_level = self.generate_reorder_level()

                maximum_stock = self.generate_maximum_stock(
                    reorder_level
                )

                unit_cost = product["Unit Cost"]

                inventory_value = round(
                    quantity * unit_cost,
                    2
                )

                last_restocked = (
                    self.generate_last_restocked_date()
                )

                record = {

                    "Inventory ID": inventory_id,

                    "Product ID": product["Product ID"],

                    "Store ID": store["Store ID"],

                    "Quantity Available": quantity,

                    "Reorder Level": reorder_level,

                    "Maximum Stock": maximum_stock,

                    "Unit Cost": unit_cost,

                    "Inventory Value": inventory_value,

                    "Last Restocked Date": last_restocked,

                    "Inventory Status":
                        self.generate_inventory_status(
                            quantity,
                            reorder_level
                        )

                }

                record["Created Date"] = (
                    last_restocked
                )

                record["Updated Date"] = (
                    CommonUtils.format_date(
                        CommonUtils.random_date(
                            last_restocked,
                            "2026-06-30"
                        )
                    )
                )

                record = self.apply_dirty_data(
                    record
                )

                rows.append(
                    record
                )

                inventory_id += 1

        return pd.DataFrame(
            rows
        )