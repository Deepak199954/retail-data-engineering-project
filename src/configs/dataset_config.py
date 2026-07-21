import random
from pathlib import Path

# ==========================================================
# Random Seed
# ==========================================================

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

OUTPUT_DIRECTORY = PROJECT_ROOT / "data" / "raw"

# ==========================================================
# Dataset Sizes
# ==========================================================

TOTAL_CUSTOMERS = 300
TOTAL_SUPPLIERS = 50
TOTAL_PRODUCTS = 200
TOTAL_STORES = 20
TOTAL_EMPLOYEES = 150
TOTAL_ORDERS = 1000

# Inventory is generated automatically from
# Product × Store relationships

# ==========================================================
# ID Ranges
# ==========================================================

CUSTOMER_ID_START = 101

SUPPLIER_ID_START = 501

PRODUCT_ID_START = 1001

STORE_ID_START = 1

EMPLOYEE_ID_START = 2001

ORDER_ID_START = 500001

INVENTORY_ID_START = 700001

ORDER_DETAIL_ID_START = 800001

PAYMENT_ID_START = 900001

# ==========================================================
# Data Generation Date Range
# ==========================================================

DATA_START_DATE = "2024-01-01"

DATA_END_DATE = "2026-07-31"

# ==========================================================
# Output File Names
# ==========================================================

CUSTOMER_FILE = "customers.csv"

SUPPLIER_FILE = "suppliers.csv"

PRODUCT_FILE = "products.csv"

STORE_FILE = "stores.csv"

EMPLOYEE_FILE = "employees.csv"

INVENTORY_FILE = "inventory.csv"

ORDER_HEADER_FILE = "orders.csv"

ORDER_DETAIL_FILE = "order_details.csv"

PAYMENT_FILE = "payments.csv"

# ==========================================================
# Dirty Data Configuration
# ==========================================================

DIRTY_DATA = {

    "customer": {

        "leading_trailing_spaces": 0.08,

        "mixed_case": 0.15,

        "duplicate_email": 0.03,

        "invalid_email": 0.03,

        "uppercase_email": 0.05,

        "future_signup_date": 0.01,

        "invalid_phone": 0.03,

        "duplicate_phone": 0.02,

        "null_city": 0.01,

        "invalid_customer_type": 0.03,

        "negative_loyalty_points": 0.01

    },

    "supplier": {

        "missing_gst": 0.02,

        "duplicate_supplier": 0.03,

        "invalid_city": 0.05,

        "leading_spaces": 0.05

    },

    "product": {

        "duplicate_product_name": 0.03,

        "missing_brand": 0.02,

        "invalid_category": 0.03,

        "mixed_category": 0.15,

        "negative_price": 0.01,

        "currency_symbol": 0.10,

        "inactive_product": 0.05

    },

    "store": {

        "duplicate_store": 0.03,

        "missing_manager": 0.05,

        "mixed_region": 0.05

    },

    "employee": {

        "future_join_date": 0.02,

        "salary_outlier": 0.02,

        "duplicate_name": 0.03,

        "missing_manager": 0.01

    },

    "inventory": {

        "negative_stock": 0.01,

        "zero_stock": 0.05,

        "duplicate_inventory": 0.02,

        "old_inventory_date": 0.05

    },

    "order": {

        "invalid_customer": 0.01,

        "invalid_product": 0.01,

        "missing_payment": 0.03,

        "future_order": 0.01,

        "negative_discount": 0.01,

        "duplicate_order": 0.02,

        "status_variation": 0.20,

        "refund_order": 0.05

    },

    "payment": {

        "failed_payment": 0.10,

        "duplicate_payment": 0.03,

        "amount_mismatch": 0.02,

        "missing_payment_date": 0.02,

        "payment_method_variation": 0.20

    }

}