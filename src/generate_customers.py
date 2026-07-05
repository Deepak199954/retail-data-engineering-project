
import random,csv,datetime

customers = []
cities = ["Pune", "Mumbai", "Bangalore", "Delhi", "Hyderabad"]
names = ["deepak","Rohit", "Shailesh", "Ravi", "Rajesh", "Rakesh", "Sanskriti", "Maihar", "Raju", "Mohit", "Jyoti", "Nilesh", "shruti", "Rutuja", "revati", "amaan", "Aakash", "Prajwal", "Sumit", "pranit"]
start_date = datetime.date(2024,1,1)
end_date = datetime.date(2025,12,31)
difference = end_date - start_date

for customer_id in range(101, 401):
    random_days = random.randint(0,difference.days)
    signup_date = start_date + datetime.timedelta(days=random_days)
    customer_name = random.choice(names)
    city = random.choice(cities)
    customer = {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "city": city,
        "signup_date" : signup_date
    }
    customers.append(customer)

print(len(customers))
print(customers[-1])

with open("customers.csv", "w", newline = "") as csv_file:
    fieldnames_value = [
        "customer_id",
        "customer_name",
        "city",
        "signup_date"
    ]
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames_value)
    writer.writeheader()
    writer.writerows(customers)
    