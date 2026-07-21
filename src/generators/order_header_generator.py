import random

import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    ORDER_STATUS,
    DELIVERY_STATUS,
    PAYMENT_METHODS
)

from utils.common import CommonUtils


class OrderHeaderGenerator:
    """
    Generates enterprise-grade Order Header data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # ORDER DATE
    # ==========================================================

    def generate_order_date(self):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                "2024-01-01",
                "2026-06-30"
            )
        )

    # ==========================================================
    # DELIVERY DATE
    # ==========================================================

    def generate_delivery_date(
            self,
            order_date
    ):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                order_date,
                "2026-07-15"
            )
        )

    # ==========================================================
    # ORDER AMOUNT
    # ==========================================================

    def generate_order_amount(self):

        return round(
            random.uniform(
                200,
                50000
            ),
            2
        )

    # ==========================================================
    # DISCOUNT
    # ==========================================================

    def generate_discount(
            self,
            order_amount
    ):

        return round(

            order_amount *

            random.uniform(
                0,
                0.30
            ),

            2

        )

    # ==========================================================
    # TAX
    # ==========================================================

    def generate_tax(
            self,
            taxable_amount
    ):

        return round(

            taxable_amount * 0.18,

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

            record["Order Amount"] = (
                -record["Order Amount"]
            )

        if random.random() < 0.01:

            record["Discount Amount"] = (
                record["Order Amount"] + 500
            )

        if random.random() < 0.01:

            record["Order Status"] = (
                CommonUtils.random_case(
                    record["Order Status"]
                )
            )

        if random.random() < 0.01:

            record["Payment Method"] = (
                "CRYPTO"
            )

        if random.random() < 0.01:

            record["Delivery Date"] = (
                CommonUtils.random_future_date()
            )

        if random.random() < 0.01:

            record["Customer ID"] = None

        return record
	# ==========================================================
    # GENERATE ORDER HEADER
    # ==========================================================

    def generate(
            self,
            customers_df,
            stores_df,
            employees_df
    ):

        rows = []

        order_id = ORDER_ID_START

        for _ in range(TOTAL_ORDERS):

            customer = customers_df.sample(1).iloc[0]

            store = stores_df.sample(1).iloc[0]

            store_employees = employees_df[
                employees_df["Store ID"] == store["Store ID"]
            ]

            if len(store_employees) > 0:

                employee = store_employees.sample(1).iloc[0]

                employee_id = employee["Employee ID"]

            else:

                employee_id = None

            order_date = self.generate_order_date()

            delivery_date = self.generate_delivery_date(
                order_date
            )

            order_amount = self.generate_order_amount()

            discount_amount = self.generate_discount(
                order_amount
            )

            taxable_amount = (
                order_amount - discount_amount
            )

            tax_amount = self.generate_tax(
                taxable_amount
            )

            net_amount = round(
                taxable_amount + tax_amount,
                2
            )

            record = {

                "Order ID": CommonUtils.generate_id(
                    "ORD",
                    order_id,
                    6
                ),

                "Customer ID": customer["Customer ID"],

                "Store ID": store["Store ID"],

                "Employee ID": employee_id,

                "Order Date": order_date,

                "Delivery Date": delivery_date,

                "Order Amount": order_amount,

                "Discount Amount": discount_amount,

                "Tax Amount": tax_amount,

                "Net Amount": net_amount,

                "Order Status": random.choice(
                    ORDER_STATUS
                ),

                "Delivery Status": random.choice(
                    DELIVERY_STATUS
                ),

                "Payment Method": random.choice(
                    PAYMENT_METHODS
                )

            }

            record["Created Date"] = order_date

            record["Updated Date"] = CommonUtils.format_date(
                CommonUtils.random_date(
                    order_date,
                    "2026-07-31"
                )
            )

            record = self.apply_dirty_data(
                record
            )

            rows.append(
                record
            )

            order_id += 1

        return pd.DataFrame(
            rows
        )