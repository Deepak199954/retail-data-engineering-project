import random
import datetime
import csv

orders = []

status = ["COMPLETED","PENDING","CANCELLED"]

product_combination = ["Laptop:Electronics","Smartphone:Electronics","Tablet:Electronics","Smartwatch:Electronics","Headphones:Electronics","Wireless Mouse:Electronics","Keyboard:Electronics","Monitor:Electronics","Office Chair:Furniture","Standing Desk:Furniture","Bookshelf:Furniture","Coffee Table:Furniture","Backpack:Accessories","Travel Bag:Accessories","Water Bottle:Accessories","Running Shoes:Footwear","Sneakers:Footwear","T-Shirt:Clothing","Jeans:Clothing","Jacket:Clothing","Blender:Home Appliances","Microwave Oven:Home Appliances","Air Fryer:Home Appliances","Electric Kettle:Home Appliances"]

start_date = datetime.date(2024,1,1)
end_date = datetime.date(2025,12,31)
difference = end_date - start_date
null_order_amount_positions = random.sample(range(1000), 20)
null_order_status_positions = random.sample(range(1000), 15)
print(difference)

for current_record_position, order_id in enumerate(range(10001, 11001)):
   product_comb = random.choice(product_combination)
   product_split = product_comb.split(":")
   product_name = (product_split[0])
   category = (product_split[1])
   if current_record_position in null_order_status_positions:
    order_status = None
   else:
    order_status = random.choice(status)
   customer_id = random.randint(101,400)
   quantity = random.randint(1,5)
   if current_record_position in null_order_amount_positions:
    order_amount = None
   else:
    order_amount = random.randint(100, 5000)
   random_days = random.randint(0, difference.days)
   order_date = start_date + datetime.timedelta(days=random_days)

   order = {
       "order_id" : order_id,
       "customer_id" : customer_id,
       "product_name" : product_name,
       "category" : category,
       "quantity" : quantity,
       "order_amount" : order_amount,
       "order_status" : order_status,
       "order_date" : order_date
   }
   orders.append(order)

print(len(orders))
print(orders[0])

with open("orders.csv","w",newline = "") as csv_file:
    fieldname_value = [
        "order_id",
        "customer_id",
        "product_name",
        "category",
        "quantity",
        "order_amount",
        "order_status",
        "order_date"
    ]
    writer = csv.DictWriter(csv_file,fieldnames = fieldname_value)
    writer.writeheader()
    writer.writerows(orders)

