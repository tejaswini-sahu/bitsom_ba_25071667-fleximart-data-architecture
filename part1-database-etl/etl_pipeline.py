import pandas as pd
import mysql.connector
from datetime import datetime
import re

# ------------------ DB CONNECTION ------------------

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tejaswini@",
    database="fleximart"
)
db_cursor = db_connection.cursor()

print("Connected to MySQL")

# ------------------ HELPERS ------------------

def format_date(value):
    if pd.isna(value):
        return None
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%m-%d-%Y", "%m/%d/%Y"]
    for fmt in date_formats:
        try:
            return datetime.strptime(str(value), fmt).strftime("%Y-%m-%d")
        except:
            pass
    return None

def format_phone(value):
    if pd.isna(value):
        return None
    digits = re.sub(r'\D', "", str(value))[-10:]
    if len(digits) == 10:
        return f"+91-{digits}"
    return None

# ------------------ EXTRACT ------------------

customers_df = pd.read_csv("data/customers_raw.csv")
products_df = pd.read_csv("data/products_raw.csv")
sales_df = pd.read_csv("data/sales_raw.csv")

# ---------------------------------------------
# COUNTERS FOR REPORT
# ---------------------------------------------

customers_count_before = len(customers_df)
products_count_before = len(products_df)
sales_count_before = len(sales_df)

customers_duplicates = customers_df.duplicated().sum()
products_duplicates = products_df.duplicated().sum()
sales_duplicates = sales_df.duplicated().sum()

missing_customer_email_count = customers_df["email"].isna().sum()
missing_product_price_count = products_df["price"].isna().sum()
missing_sales_fk_count = (
    sales_df["customer_id"].isna().sum() +
    sales_df["product_id"].isna().sum()
)

# ------------------ TRANSFORM ------------------

# ===== CUSTOMERS =====
customers_df = customers_df.drop_duplicates()
customers_df = customers_df[customers_df["email"].notna()]
customers_df["phone"] = customers_df["phone"].apply(format_phone)
customers_df["registration_date"] = customers_df["registration_date"].apply(format_date)
customers_df["city"] = customers_df["city"].str.title()

# ===== PRODUCTS =====
products_df = products_df.drop_duplicates()

products_df["product_name"] = (
    products_df["product_name"]
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

products_df["category"] = products_df["category"].str.lower().replace({
    "electronics": "Electronics",
    "fashion": "Fashion",
    "groceries": "Groceries"
})

products_df = products_df[products_df["price"].notna()]
products_df["stock_quantity"] = products_df["stock_quantity"].fillna(0)

# ===== SALES =====
sales_df = sales_df.drop_duplicates()
sales_df = sales_df.dropna(subset=["customer_id", "product_id"])
sales_df = sales_df[sales_df["status"] != "Cancelled"]
sales_df["transaction_date"] = sales_df["transaction_date"].apply(format_date)
sales_df["subtotal"] = sales_df["quantity"] * sales_df["unit_price"]

print("Data cleaned")

# ------------------ LOAD ------------------

customer_code_map = {}

for _, row in customers_df.iterrows():
    db_cursor.execute("""
        INSERT IGNORE INTO customers(first_name,last_name,email,phone,city,registration_date)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        row["first_name"],
        row["last_name"],
        row["email"],
        row["phone"],
        row["city"],
        row["registration_date"]
    ))

    db_id = db_cursor.lastrowid

    if db_id == 0:
        db_cursor.execute(
            "SELECT customer_id FROM customers WHERE email=%s",
            (row["email"],)
        )
        db_id = db_cursor.fetchone()[0]

    customer_code_map[row["customer_id"]] = db_id

db_connection.commit()

product_code_map = {}

for _, row in products_df.iterrows():
    db_cursor.execute("""
        INSERT INTO products(product_name,category,price,stock_quantity)
        VALUES (%s,%s,%s,%s)
    """, (
        row["product_name"],
        row["category"],
        row["price"],
        int(row["stock_quantity"])
    ))

    product_code_map[row["product_id"]] = db_cursor.lastrowid

db_connection.commit()

valid_customer_codes = set(customer_code_map.keys())
valid_product_codes = set(product_code_map.keys())

sales_df = sales_df[sales_df["customer_id"].isin(valid_customer_codes)]
sales_df = sales_df[sales_df["product_id"].isin(valid_product_codes)]

unique_transactions = sales_df["transaction_id"].unique()

orders_inserted = 0
order_items_inserted = 0

for transaction_id in unique_transactions:

    transaction_rows = sales_df[sales_df["transaction_id"] == transaction_id]

    customer_code = transaction_rows.iloc[0]["customer_id"]
    customer_db_id = customer_code_map.get(customer_code)

    if customer_db_id is None:
        continue

    order_date = transaction_rows.iloc[0]["transaction_date"]
    order_status = transaction_rows.iloc[0]["status"]
    order_total = transaction_rows["subtotal"].sum()

    db_cursor.execute("""
        INSERT INTO orders(customer_id, order_date, total_amount, status)
        VALUES (%s,%s,%s,%s)
    """, (int(customer_db_id), order_date, order_total, order_status))

    order_id = db_cursor.lastrowid
    orders_inserted += 1

    for _, row in transaction_rows.iterrows():

        product_code = row["product_id"]
        product_db_id = product_code_map.get(product_code)

        if product_db_id is None:
            continue

        db_cursor.execute("""
            INSERT INTO order_items(order_id, product_id, quantity, unit_price, subtotal)
            VALUES (%s,%s,%s,%s,%s)
        """, (
            order_id,
            int(product_db_id),
            int(row["quantity"]),
            row["unit_price"],
            row["subtotal"]
        ))

        order_items_inserted += 1

db_connection.commit()

# ------------------ DATA QUALITY REPORT ------------------

with open("part1-database-etl/data_quality_report.txt", "w") as report_file:

    report_file.write("FlexiMart Data Quality Report\n")
    report_file.write("---------------------------------\n\n")

    report_file.write("Number of records processed per file:\n")
    report_file.write(f"  Customers processed: {customers_count_before}\n")
    report_file.write(f"  Products processed: {products_count_before}\n")
    report_file.write(f"  Sales processed: {sales_count_before}\n\n")

    report_file.write("Number of duplicates removed:\n")
    report_file.write(f"  Customer duplicates removed: {customers_duplicates}\n")
    report_file.write(f"  Product duplicates removed: {products_duplicates}\n")
    report_file.write(f"  Sales duplicates removed: {sales_duplicates}\n\n")

    report_file.write("Number of missing values handled:\n")
    report_file.write(f"  Missing customer emails removed: {missing_customer_email_count}\n")
    report_file.write(f"  Missing product prices removed: {missing_product_price_count}\n")
    report_file.write(f"  Missing sales FK rows removed: {missing_sales_fk_count}\n\n")

    report_file.write("Number of records loaded successfully:\n")
    report_file.write(f"  Customers loaded: {len(customers_df)}\n")
    report_file.write(f"  Products loaded: {len(products_df)}\n")
    report_file.write(f"  Orders loaded: {orders_inserted}\n")
    report_file.write(f"  Order items loaded: {order_items_inserted}\n")

db_cursor.close()
db_connection.close()

print("ETL completed successfully and report generated.")
