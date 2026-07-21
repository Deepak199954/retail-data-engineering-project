
import random


import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    PRODUCT_HIERARCHY,
    PRODUCT_BRANDS,
    WARRANTY_OPTIONS,
    GST_OPTIONS,
    PRODUCT_STATUS
)

from utils.common import CommonUtils


class ProductGenerator:
    """
    Generates enterprise-grade Product Master data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # PRODUCT HIERARCHY
    # ==========================================================

    def get_product_details(self):

        category = random.choice(
            list(PRODUCT_HIERARCHY.keys())
        )

        sub_category = random.choice(
            list(PRODUCT_HIERARCHY[category].keys())
        )

        product_name = random.choice(
            PRODUCT_HIERARCHY[category][sub_category]
        )

        brand = random.choice(
            PRODUCT_BRANDS
        )

        return (
            category,
            sub_category,
            product_name,
            brand
        )

    # ==========================================================
    # SKU
    # ==========================================================

    def generate_sku(
            self,
            category,
            sub_category,
            product_id
    ):

        cat = category[:3].upper()

        sub = sub_category[:3].upper()

        return (
            f"SKU-{cat}-{sub}-"
            f"{product_id:05d}"
        )

    # ==========================================================
    # COST PRICE
    # ==========================================================

    def generate_cost_price(
            self,
            category
    ):

        if category == "Electronics":

            return random.randint(
                8000,
                90000
            )

        elif category == "Home Appliances":

            return random.randint(
                2500,
                45000
            )

        elif category == "Fashion":

            return random.randint(
                300,
                4000
            )

        elif category == "Footwear":

            return random.randint(
                400,
                5000
            )

        elif category == "Beauty":

            return random.randint(
                80,
                1800
            )

        elif category == "Books":

            return random.randint(
                150,
                1200
            )

        else:

            return random.randint(
                100,
                2500
            )

    # ==========================================================
    # SELLING PRICE
    # ==========================================================

    def generate_selling_price(
            self,
            cost_price
    ):

        margin = random.uniform(
            0.15,
            0.45
        )

        selling_price = cost_price * (
                1 + margin
        )

        return round(
            selling_price,
            2
        )

    # ==========================================================
    # MARGIN
    # ==========================================================

    def generate_margin(
            self,
            cost_price,
            selling_price
    ):

        return round(

            (
                    (
                            selling_price - cost_price
                    )
                    /
                    cost_price
            )
            * 100,

            2

        )

    # ==========================================================
    # WEIGHT
    # ==========================================================

    def generate_weight(
            self,
            category
    ):

        if category == "Electronics":

            return round(
                random.uniform(
                    0.20,
                    8.00
                ),
                2
            )

        elif category == "Home Appliances":

            return round(
                random.uniform(
                    2,
                    45
                ),
                2
            )

        elif category == "Fashion":

            return round(
                random.uniform(
                    0.15,
                    1.50
                ),
                2
            )

        elif category == "Footwear":

            return round(
                random.uniform(
                    0.30,
                    2.00
                ),
                2
            )

        else:

            return round(
                random.uniform(
                    0.10,
                    3.00
                ),
                2
            )

    # ==========================================================
    # DATES
    # ==========================================================

    def generate_launch_date(self):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                "2020-01-01",
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

            record["Brand"] = None

        if random.random() < 0.02:

            record["GST %"] = 35

        if random.random() < 0.01:

            record["Unit Cost"] = (
                -record["Unit Cost"]
            )

        if random.random() < 0.01:

            record["Selling Price"] = (
                record["Unit Cost"] - 500
            )

        if random.random() < 0.02:

            record["Category"] = (
                CommonUtils.random_case(
                    record["Category"]
                )
            )

        if random.random() < 0.01:

            record["Launch Date"] = (
                CommonUtils.random_future_date()
            )

        return record
        
    # ==========================================================
    # GENERATE PRODUCT MASTER
    # ==========================================================

    def generate(self):

        rows = []

        product_id = PRODUCT_ID_START

        for _ in range(TOTAL_PRODUCTS):

            (
                category,
                sub_category,
                product_name,
                brand
            ) = self.get_product_details()

            sku = self.generate_sku(
                category,
                sub_category,
                product_id
            )

            supplier_id = random.randint(
                SUPPLIER_ID_START,
                SUPPLIER_ID_START + TOTAL_SUPPLIERS - 1
            )

            cost_price = self.generate_cost_price(
                category
            )

            selling_price = self.generate_selling_price(
                cost_price
            )

            margin = self.generate_margin(
                cost_price,
                selling_price
            )

            record = {

                "Product ID": CommonUtils.generate_id(
                    "PROD",
                    product_id,
                    5
                ),

                "SKU": sku,

                "Product Name": product_name,

                "Category": category,

                "Sub Category": sub_category,

                "Brand": brand,

                "Supplier ID": CommonUtils.generate_id(
                    "SUP",
                    supplier_id,
                    5
                ),

                "Unit Cost": cost_price,

                "Selling Price": selling_price,

                "Profit Margin %": margin,

                "GST %": random.choice(
                    GST_OPTIONS
                ),

                "Weight (Kg)": self.generate_weight(
                    category
                ),

                "Warranty (Months)": random.choice(
                    WARRANTY_OPTIONS
                ),

                "Launch Date": self.generate_launch_date(),

                "Product Status": random.choice(
                    PRODUCT_STATUS
                )

            }

            record["Created Date"] = record["Launch Date"]

            record["Updated Date"] = CommonUtils.format_date(
                CommonUtils.random_date(
                    record["Launch Date"],
                    "2026-06-30"
                )
            )

            record = self.apply_dirty_data(
                record
            )

            rows.append(
                record
            )

            product_id += 1

        return pd.DataFrame(
            rows
        )