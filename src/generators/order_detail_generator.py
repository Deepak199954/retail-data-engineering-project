"""
==========================================================
RetailMart Order Detail Generator
Author : ChatGPT
==========================================================
"""

import random

import pandas as pd

from configs.dataset_config import *

from utils.common import CommonUtils


class OrderDetailGenerator:
    """
    Generates enterprise-grade Order Detail data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # QUANTITY
    # ==========================================================

    def generate_quantity(self):

        return random.randint(
            1,
            5
        )

    # ==========================================================
    # DISCOUNT %
    # ==========================================================

    def generate_discount_percent(self):

        return random.choice(
            [
                0,
                5,
                10,
                15,
                20
            ]
        )

    # ==========================================================
    # TAX %
    # ==========================================================

    def generate_tax_percent(
            self,
            product
    ):

        return product["GST %"]

    # ==========================================================
    # LINE TOTAL
    # ==========================================================

    def calculate_line_total(
            self,
            quantity,
            unit_price,
            discount_amount,
            tax_amount
    ):

        return round(

            (
                quantity * unit_price
            )
            -
            discount_amount
            +
            tax_amount,

            2

        )

    # ==========================================================
    # DIRTY DATA
    # ==========================================================

    def apply_dirty_data(
            self,
            record
    ):

        if random.random() < 0.01:

            record["Quantity"] = -record["Quantity"]

        if random.random() < 0.01:

            record["Unit Price"] = (
                -record["Unit Price"]
            )

        if random.random() < 0.01:

            record["Discount %"] = 150

        if random.random() < 0.01:

            record["Tax %"] = 50

        if random.random() < 0.01:

            record["Line Total"] = -100

        return record
    # ==========================================================
    # GENERATE ORDER DETAILS
    # ==========================================================

    def generate(
            self,
            orders_df,
            inventory_df,
            products_df
    ):

        rows = []

        order_detail_id = ORDER_DETAIL_ID_START

        for _, order in orders_df.iterrows():

            store_inventory = inventory_df[
                inventory_df["Store ID"] == order["Store ID"]
            ]

            if store_inventory.empty:
                continue

            max_products = min(
                len(store_inventory),
                random.randint(1, 5)
            )

            selected_inventory = store_inventory.sample(
                n=max_products,
                replace=False
            )

            for _, inventory in selected_inventory.iterrows():

                product = products_df[
                    products_df["Product ID"] ==
                    inventory["Product ID"]
                ].iloc[0]

                quantity = self.generate_quantity()

                unit_price = product["Selling Price"]

                discount_percent = (
                    self.generate_discount_percent()
                )

                discount_amount = round(
                    (
                        quantity *
                        unit_price *
                        discount_percent
                    ) / 100,
                    2
                )

                tax_percent = self.generate_tax_percent(
                    product
                )

                taxable_amount = (
                    quantity * unit_price
                ) - discount_amount

                tax_amount = round(
                    taxable_amount *
                    tax_percent / 100,
                    2
                )

                line_total = self.calculate_line_total(
                    quantity,
                    unit_price,
                    discount_amount,
                    tax_amount
                )

                record = {

                    "Order Detail ID": order_detail_id,

                    "Order ID": order["Order ID"],

                    "Product ID": product["Product ID"],

                    "Quantity": quantity,

                    "Unit Price": unit_price,

                    "Discount %": discount_percent,

                    "Discount Amount": discount_amount,

                    "Tax %": tax_percent,

                    "Tax Amount": tax_amount,

                    "Line Total": line_total

                }

                record["Created Date"] = (
                    order["Order Date"]
                )

                record["Updated Date"] = (
                    CommonUtils.format_date(
                        CommonUtils.random_date(
                            order["Order Date"],
                            "2026-07-31"
                        )
                    )
                )

                record = self.apply_dirty_data(
                    record
                )

                rows.append(
                    record
                )

                order_detail_id += 1

        return pd.DataFrame(
            rows
        )