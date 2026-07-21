
from configs.dataset_config import OUTPUT_DIRECTORY

from generators.customer_generator import CustomerGenerator
from generators.supplier_generator import SupplierGenerator
from generators.product_generator import ProductGenerator
from generators.store_generator import StoreGenerator
from generators.employee_generator import EmployeeGenerator
from generators.inventory_generator import InventoryGenerator
from generators.order_header_generator import OrderHeaderGenerator
from generators.order_detail_generator import OrderDetailGenerator
from generators.payment_generator import PaymentGenerator


class DatasetGenerator:

    def __init__(self):

        OUTPUT_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )

    ########################################################

    def save_dataset(self, dataframe, filename):

        output_file = OUTPUT_DIRECTORY / filename

        dataframe.to_csv(
            output_file,
            index=False
        )

        print("=" * 70)
        print(f"Dataset : {filename}")
        print(f"Rows    : {len(dataframe)}")
        print(f"Saved   : {output_file}")

    ########################################################

    def generate_customers(self):

        print("\nGenerating Customer Master...")

        df = CustomerGenerator().generate()

        self.save_dataset(
            df,
            "CRM_Customer_Master_2026.csv"
        )

        return df

    ########################################################

    def generate_suppliers(self):

        print("\nGenerating Supplier Master...")

        df = SupplierGenerator().generate()

        self.save_dataset(
            df,
            "Vendor_Supplier_Master_2026.csv"
        )

        return df

    ########################################################

    def generate_products(self):

        print("\nGenerating Product Master...")

        df = ProductGenerator().generate()

        self.save_dataset(
            df,
            "ERP_Product_Master_2026.csv"
        )

        return df

    ########################################################

    def generate_stores(self):

        print("\nGenerating Store Master...")

        df = StoreGenerator().generate()

        self.save_dataset(
            df,
            "Retail_Store_Master_2026.csv"
        )

        return df

    ########################################################

    def generate_employees(self, stores_df):

        print("\nGenerating Employee Master...")

        df = EmployeeGenerator().generate(
            stores_df
        )

        self.save_dataset(
            df,
            "HR_Employee_Master_2026.csv"
        )

        return df

    ########################################################

    def generate_inventory(
            self,
            stores_df,
            products_df
    ):

        print("\nGenerating Inventory...")

        df = InventoryGenerator().generate(
            stores_df,
            products_df
        )

        self.save_dataset(
            df,
            "Inventory_Stock_2026.csv"
        )

        return df

    ########################################################

    def generate_order_headers(
            self,
            customers_df,
            stores_df,
            employees_df
    ):

        print("\nGenerating Order Headers...")

        df = OrderHeaderGenerator().generate(
            customers_df,
            stores_df,
            employees_df
        )

        self.save_dataset(
            df,
            "Sales_Order_Header_2026.csv"
        )

        return df

    ########################################################

    def generate_order_details(
            self,
            orders_df,
            inventory_df,
            products_df
    ):

        print("\nGenerating Order Details...")

        df = OrderDetailGenerator().generate(
            orders_df,
            inventory_df,
            products_df
        )

        self.save_dataset(
            df,
            "Sales_Order_Detail_2026.csv"
        )

        return df

    ########################################################

    def generate_payments(
            self,
            orders_df
    ):

        print("\nGenerating Payments...")

        df = PaymentGenerator().generate(
            orders_df
        )

        self.save_dataset(
            df,
            "Finance_Payment_2026.csv"
        )

        return df

    ########################################################

    def generate_all(self):

        print("=" * 70)
        print("RetailMart Dataset Generation Started")
        print("=" * 70)

        customers_df = self.generate_customers()

        suppliers_df = self.generate_suppliers()

        products_df = self.generate_products()

        stores_df = self.generate_stores()

        employees_df = self.generate_employees(
            stores_df
        )

        inventory_df = self.generate_inventory(
            stores_df,
            products_df
        )

        orders_df = self.generate_order_headers(
            customers_df,
            stores_df,
            employees_df
        )

        order_details_df = self.generate_order_details(
            orders_df,
            inventory_df,
            products_df
        )

        payments_df = self.generate_payments(
            orders_df
        )

        print("\n")
        print("=" * 70)
        print("Dataset Generation Completed Successfully")
        print("=" * 70)


############################################################


def main():

    generator = DatasetGenerator()

    generator.generate_all()


############################################################

if __name__ == "__main__":

    main()