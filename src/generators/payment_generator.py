import random

import pandas as pd

from configs.dataset_config import *
from configs.master_data import (
    PAYMENT_METHODS,
    PAYMENT_STATUS,
    BANKS
)

from utils.common import CommonUtils


class PaymentGenerator:
    """
    Generates enterprise-grade Payment data.
    """

    def __init__(self):

        random.seed(RANDOM_SEED)

    # ==========================================================
    # PAYMENT DATE
    # ==========================================================

    def generate_payment_date(
            self,
            order_date
    ):

        return CommonUtils.format_date(
            CommonUtils.random_date(
                order_date,
                "2026-07-31"
                )
        )

    # ==========================================================
    # TRANSACTION REFERENCE
    # ==========================================================

    def generate_transaction_reference(self):

        return (
            "TXN"
            +
            str(
                random.randint(
                    100000000,
                    999999999
                )
            )
        )

    # ==========================================================
    # BANK NAME
    # ==========================================================

    def generate_bank(self):

        return random.choice(
            BANKS
        )

    # ==========================================================
    # DIRTY DATA
    # ==========================================================

    def apply_dirty_data(
            self,
            record
    ):

        if random.random() < 0.01:

            record["Payment Amount"] = (
                -record["Payment Amount"]
            )

        if random.random() < 0.01:

            record["Payment Status"] = (
                CommonUtils.random_case(
                    record["Payment Status"]
                )
            )

        if random.random() < 0.01:

            record["Payment Method"] = (
                "CRYPTO"
            )

        if random.random() < 0.01:

            record["Transaction Reference"] = (
                None
            )

        if random.random() < 0.01:

            record["Payment Date"] = (
                CommonUtils.random_future_date()
            )

        return record
	# ==========================================================
    # GENERATE PAYMENT DATA
    # ==========================================================

    def generate(
            self,
            orders_df
    ):

        rows = []

        payment_id = PAYMENT_ID_START

        payment_weights = [

            0.88,   # PAID
            0.06,   # PENDING
            0.03,   # FAILED
            0.03    # REFUNDED

        ]

        for _, order in orders_df.iterrows():

            payment_status = random.choices(

                PAYMENT_STATUS,

                weights=payment_weights,

                k=1

            )[0]

            payment_date = self.generate_payment_date(

                order["Order Date"]

            )

            record = {

                "Payment ID": CommonUtils.generate_id(
                    "PAY",
                    payment_id,
                    6
                ),

                "Order ID": order["Order ID"],

                "Payment Date": payment_date,

                "Payment Method": random.choice(
                    PAYMENT_METHODS
                ),

                "Payment Amount": order["Net Amount"],

                "Payment Status": payment_status,

                "Transaction Reference":
                    self.generate_transaction_reference(),

                "Bank Name": self.generate_bank()

            }

            record["Created Date"] = payment_date

            record["Updated Date"] = CommonUtils.format_date(
                CommonUtils.random_date(
                    payment_date,
                    "2026-07-31"
                )
            )

            record = self.apply_dirty_data(

                record

            )

            rows.append(

                record

            )

            payment_id += 1

        return pd.DataFrame(

            rows

        )