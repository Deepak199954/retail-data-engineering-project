"""
==========================================================
RetailMart Master Data
Author : ChatGPT
==========================================================
"""

# ==========================================================
# INDIA GEOGRAPHY
# ==========================================================

STATE_CITY = {

    "Maharashtra": [
        "Mumbai",
        "Pune",
        "Nagpur",
        "Nashik"
    ],

    "Karnataka": [
        "Bengaluru",
        "Mysuru",
        "Hubli",
        "Mangalore"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Coimbatore",
        "Madurai",
        "Salem"
    ],

    "Delhi": [
        "New Delhi"
    ],

    "Gujarat": [
        "Ahmedabad",
        "Surat",
        "Vadodara",
        "Rajkot"
    ]

}

# ==========================================================
# PRODUCT HIERARCHY
# ==========================================================

PRODUCT_HIERARCHY = {

    "Electronics": {

        "Mobile Phones": [

            "Galaxy S24 Ultra",
            "Galaxy A55",
            "iPhone 15",
            "iPhone 15 Pro",
            "Redmi Note 13",
            "OnePlus 12",
            "Nothing Phone 2",
            "Moto Edge 50"

        ],

        "Laptops": [

            "MacBook Air M3",
            "Inspiron 15",
            "ThinkPad E14",
            "Pavilion 15",
            "IdeaPad Slim 5",
            "Vivobook 15"

        ],

        "Television": [

            "Smart LED TV",
            "OLED TV",
            "QLED TV",
            "Android TV"

        ],

        "Tablets": [

            "iPad Air",
            "Galaxy Tab",
            "Lenovo Tab",
            "Xiaomi Pad"

        ]

    },

    "Home Appliances": {

        "Kitchen": [

            "Mixer Grinder",
            "Air Fryer",
            "Microwave Oven",
            "Induction Cooktop",
            "Juicer"

        ],

        "Cleaning": [

            "Vacuum Cleaner",
            "Steam Mop"

        ],

        "Cooling": [

            "Air Conditioner",
            "Ceiling Fan",
            "Air Cooler"

        ],

        "Laundry": [

            "Washing Machine"

        ]

    },

    "Fashion": {

        "Men": [

            "Formal Shirt",
            "Casual Shirt",
            "Jeans",
            "T-Shirt",
            "Jacket"

        ],

        "Women": [

            "Kurti",
            "Top",
            "Jeans",
            "Dress",
            "Saree"

        ],

        "Kids": [

            "Kids T-Shirt",
            "School Uniform",
            "Kids Jeans"

        ]

    },

    "Footwear": {

        "Sports Shoes": [

            "Running Shoes",
            "Training Shoes",
            "Walking Shoes"

        ],

        "Casual Shoes": [

            "Sneakers",
            "Loafers"

        ],

        "Sandals": [

            "Men Sandals",
            "Women Sandals"

        ]

    },

    "Grocery": {

        "Rice": [

            "Basmati Rice",
            "Premium Rice",
            "Brown Rice"

        ],

        "Pulses": [

            "Toor Dal",
            "Moong Dal",
            "Chana Dal"

        ],

        "Oil": [

            "Sunflower Oil",
            "Groundnut Oil",
            "Mustard Oil"

        ],

        "Beverages": [

            "Tea",
            "Coffee",
            "Green Tea"

        ]

    },

    "Beauty": {

        "Skin Care": [

            "Face Wash",
            "Moisturizer",
            "Sunscreen"

        ],

        "Hair Care": [

            "Shampoo",
            "Hair Oil",
            "Conditioner"

        ],

        "Fragrance": [

            "Perfume",
            "Deodorant"

        ]

    },

    "Books": {

        "Technology": [

            "Python Programming",
            "Spark Essentials",
            "SQL Handbook"

        ],

        "Business": [

            "Rich Dad Poor Dad",
            "Atomic Habits",
            "The Lean Startup"

        ]

    }

}

# ==========================================================
# PRODUCT BRANDS
# ==========================================================

PRODUCT_BRANDS = [

    "Apple",
    "Samsung",
    "OnePlus",
    "Xiaomi",
    "Lenovo",
    "Dell",
    "HP",
    "Asus",
    "Sony",
    "LG",
    "Whirlpool",
    "IFB",
    "Prestige",
    "Philips",
    "Nike",
    "Adidas",
    "Puma",
    "Levis",
    "Allen Solly",
    "Raymond",
    "Himalaya",
    "Nivea",
    "Mamaearth",
    "Tata",
    "Fortune",
    "Aashirvaad"

]

# ==========================================================
# PRODUCT ATTRIBUTES
# ==========================================================

WARRANTY_OPTIONS = [

    0,
    6,
    12,
    18,
    24,
    36

]

GST_OPTIONS = [

    0,
    5,
    12,
    18,
    28

]

PRODUCT_STATUS = [

    "ACTIVE",
    "ACTIVE",
    "ACTIVE",
    "ACTIVE",
    "DISCONTINUED"

]

# ==========================================================
# HR MASTER
# ==========================================================

DEPARTMENTS = [

    "Sales",
    "Finance",
    "Human Resources",
    "Operations",
    "Supply Chain",
    "Procurement",
    "IT",
    "Customer Support"

]

DESIGNATIONS = [

    "Associate",
    "Senior Associate",
    "Executive",
    "Senior Executive",
    "Lead",
    "Assistant Manager",
    "Manager"

]

# ==========================================================
# SUPPLIER MASTER
# ==========================================================

SUPPLIER_NAMES = [

    "ABC Distributors Pvt Ltd",
    "Global Retail Supplies",
    "Prime Wholesale Traders",
    "National Electronics",
    "Universal Suppliers",
    "Shree Enterprises",
    "Sunrise Distributors",
    "Metro Wholesale",
    "Elite Traders",
    "Blue Star Suppliers",
    "Future Retail Distribution",
    "Infinity Traders",
    "Super Wholesale",
    "NextGen Supplies",
    "Apex Distributors",
    "Galaxy Trading Company",
    "Supreme Wholesale",
    "City Distributors",
    "Royal Supply Chain",
    "Om Enterprises"

]

PAYMENT_TERMS = [

    "Advance",
    "Net 15",
    "Net 30",
    "Net 45",
    "Net 60"

]

SUPPLIER_RATING = [

    1,
    2,
    3,
    4,
    5

]

# ==========================================================
# STORE MASTER
# ==========================================================

STORE_NAMES = [

    "RetailMart Phoenix Mall",
    "RetailMart City Center",
    "RetailMart Metro Plaza",
    "RetailMart Grand Mall",
    "RetailMart High Street",
    "RetailMart Central",
    "RetailMart Express",
    "RetailMart Hyper",
    "RetailMart Signature",
    "RetailMart Galleria",
    "RetailMart Infinity",
    "RetailMart Downtown",
    "RetailMart Skyline",
    "RetailMart Lakeside",
    "RetailMart Crown",
    "RetailMart Pavilion",
    "RetailMart Horizon",
    "RetailMart Mega Store",
    "RetailMart One",
    "RetailMart Prime"

]

STORE_TYPES = [

    "Hypermarket",
    "Supermarket",
    "Express Store"

]

REGIONS = {

    "Delhi": "North",

    "Maharashtra": "West",

    "Gujarat": "West",

    "Tamil Nadu": "South",

    "Karnataka": "South"

}

STORE_STATUS = [

    "ACTIVE",
    "ACTIVE",
    "ACTIVE",
    "ACTIVE",
    "UNDER RENOVATION"

]

# ==========================================================
# EMPLOYEE MASTER
# ==========================================================

EMPLOYMENT_TYPES = [

    "Permanent",
    "Contract"

]

EMPLOYEE_STATUS = [

    "ACTIVE",
    "ACTIVE",
    "ACTIVE",
    "ON LEAVE",
    "RESIGNED"

]

# ==========================================================
# ORDER MASTER
# ==========================================================

ORDER_STATUS = [

    "PLACED",
    "CONFIRMED",
    "PACKED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"

]

DELIVERY_STATUS = [

    "NOT SHIPPED",
    "IN TRANSIT",
    "DELIVERED",
    "RETURNED"

]

# ==========================================================
# PAYMENT MASTER
# ==========================================================

PAYMENT_METHODS = [

    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash",
    "Wallet"

]

PAYMENT_STATUS = [

    "SUCCESS",
    "PENDING",
    "FAILED",
    "REFUNDED"

]

BANKS = [

    "HDFC Bank",
    "ICICI Bank",
    "State Bank of India",
    "Axis Bank",
    "Kotak Mahindra Bank",
    "Punjab National Bank"

]

# ==========================================================
# INVENTORY MASTER
# ==========================================================

INVENTORY_STATUS = [

    "AVAILABLE",
    "LOW STOCK",
    "OUT OF STOCK"

]

# ==========================================================
# CUSTOMER MASTER
# ==========================================================

CUSTOMER_TYPES = [

    "Regular",
    "Premium",
    "Gold"

]

CUSTOMER_STATUS = [

    "ACTIVE",
    "ACTIVE",
    "ACTIVE",
    "INACTIVE"

]

# ==========================================================
# COURIER PARTNERS
# ==========================================================

COURIER_PARTNERS = [

    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ecom Express",
    "XpressBees",
    "India Post"

]