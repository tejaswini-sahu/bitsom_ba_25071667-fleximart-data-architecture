USE fleximart_dw;

-------------------------------
-- DIM DATE (30 dates)
-------------------------------

INSERT INTO dim_date(date_key, full_date, day_of_week, day_of_month, month, month_name, quarter, year, is_weekend) VALUES
(20240301, '2024-03-01', 'Friday', 1, 3, 'March', 'Q1', 2024, 0),
(20240302, '2024-03-02', 'Saturday', 2, 3, 'March', 'Q1', 2024, 1),
(20240303, '2024-03-03', 'Sunday', 3, 3, 'March', 'Q1', 2024, 1),
(20240304, '2024-03-04', 'Monday', 4, 3, 'March', 'Q1', 2024, 0),
(20240305, '2024-03-05', 'Tuesday', 5, 3, 'March', 'Q1', 2024, 0),

(20240306, '2024-03-06', 'Wednesday', 6, 3, 'March', 'Q1', 2024, 0),
(20240307, '2024-03-07', 'Thursday', 7, 3, 'March', 'Q1', 2024, 0),
(20240308, '2024-03-08', 'Friday', 8, 3, 'March', 'Q1', 2024, 0),
(20240309, '2024-03-09', 'Saturday', 9, 3, 'March', 'Q1', 2024, 1),
(20240310, '2024-03-10', 'Sunday', 10, 3, 'March', 'Q1', 2024, 1),

(20240311, '2024-03-11', 'Monday', 11, 3, 'March', 'Q1', 2024, 0),
(20240312, '2024-03-12', 'Tuesday', 12, 3, 'March', 'Q1', 2024, 0),
(20240313, '2024-03-13', 'Wednesday', 13, 3, 'March', 'Q1', 2024, 0),
(20240314, '2024-03-14', 'Thursday', 14, 3, 'March', 'Q1', 2024, 0),
(20240315, '2024-03-15', 'Friday', 15, 3, 'March', 'Q1', 2024, 0),

(20240316, '2024-03-16', 'Saturday', 16, 3, 'March', 'Q1', 2024, 1),
(20240317, '2024-03-17', 'Sunday', 17, 3, 'March', 'Q1', 2024, 1),
(20240318, '2024-03-18', 'Monday', 18, 3, 'March', 'Q1', 2024, 0),
(20240319, '2024-03-19', 'Tuesday', 19, 3, 'March', 'Q1', 2024, 0),
(20240320, '2024-03-20', 'Wednesday', 20, 3, 'March', 'Q1', 2024, 0),

(20240321, '2024-03-21', 'Thursday', 21, 3, 'March', 'Q1', 2024, 0),
(20240322, '2024-03-22', 'Friday', 22, 3, 'March', 'Q1', 2024, 0),
(20240323, '2024-03-23', 'Saturday', 23, 3, 'March', 'Q1', 2024, 1),
(20240324, '2024-03-24', 'Sunday', 24, 3, 'March', 'Q1', 2024, 1),
(20240325, '2024-03-25', 'Monday', 25, 3, 'March', 'Q1', 2024, 0),

(20240326, '2024-03-26', 'Tuesday', 26, 3, 'March', 'Q1', 2024, 0),
(20240327, '2024-03-27', 'Wednesday', 27, 3, 'March', 'Q1', 2024, 0),
(20240328, '2024-03-28', 'Thursday', 28, 3, 'March', 'Q1', 2024, 0),
(20240329, '2024-03-29', 'Friday', 29, 3, 'March', 'Q1', 2024, 0),
(20240330, '2024-03-30', 'Saturday', 30, 3, 'March', 'Q1', 2024, 1);

-------------------------------
-- DIM PRODUCT (15 products)
-------------------------------

INSERT INTO dim_product(product_id, product_name, category, subcategory, unit_price) VALUES
('ELEC101','OnePlus 11','Electronics','Smartphone',69999.00),
('ELEC102','Google Pixel 8','Electronics','Smartphone',75999.00),
('ELEC103','HP Pavilion Laptop','Electronics','Laptop',60999.00),
('ELEC104','JBL Bluetooth Speaker','Electronics','Audio',4999.00),
('ELEC105','Samsung 43 inch TV','Electronics','Television',45999.00),

('GROC101','Aashirvaad Atta 5kg','Groceries','Food Grains',399.00),
('GROC102','Tata Tea Gold 1kg','Groceries','Beverages',540.00),
('GROC103','Surf Excel 2kg','Groceries','Household',420.00),
('GROC104','Mother Dairy Milk 1L','Groceries','Dairy',64.00),
('GROC105','Kissan Jam 500g','Groceries','Spreads',155.00),

('FASH101','Roadster Jacket','Fashion','Clothing',4499.00),
('FASH102','Puma Sneakers','Fashion','Footwear',6499.00),
('FASH103','Van Heusen Shirt','Fashion','Clothing',2899.00),
('FASH104','UCB Polo T-shirt','Fashion','Clothing',1999.00),
('FASH105','HRX Track Pants','Fashion','Clothing',2299.00);

-------------------------------
-- DIM CUSTOMER (12 customers)
-------------------------------

INSERT INTO dim_customer(customer_id, customer_name, city, state, customer_segment) VALUES
('CU101','Ankit Agarwal','Noida','Uttar Pradesh','Premium'),
('CU102','Riya Shah','Mumbai','Maharashtra','Gold'),
('CU103','Suresh Iyer','Chennai','Tamil Nadu','Regular'),
('CU104','Pooja Malhotra','Delhi','Delhi','Premium'),
('CU105','Kunal Jain','Indore','Madhya Pradesh','Regular'),
('CU106','Ayesha Khan','Bhopal','Madhya Pradesh','Regular'),
('CU107','Nikhil Patil','Kolhapur','Maharashtra','Gold'),
('CU108','Meera Pillai','Trivandrum','Kerala','Premium'),
('CU109','Rohan Das','Kolkata','West Bengal','Regular'),
('CU110','Simran Kaur','Amritsar','Punjab','Regular'),
('CU111','Harsh Mehta','Rajkot','Gujarat','Gold'),
('CU112','Tanvi Kulkarni','Nashik','Maharashtra','Premium');

-------------------------------
-- FACT SALES (40 rows)
-------------------------------

INSERT INTO fact_sales(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount) VALUES
(20240302,1,1,2,69999,1000,139998),
(20240303,2,2,1,75999,0,75999),
(20240304,3,3,1,60999,0,60999),
(20240305,4,4,3,4999,500,14497),
(20240306,5,5,1,45999,0,45999),

(20240309,6,6,6,399,0,2394),
(20240310,7,7,2,540,0,1080),
(20240311,8,8,3,420,0,1260),
(20240312,9,9,5,64,0,320),
(20240313,10,10,4,155,100,520),

(20240316,11,11,1,4499,0,4499),
(20240317,12,12,2,6499,500,12498),
(20240318,13,1,2,2899,0,5798),
(20240319,14,2,3,1999,0,5997),
(20240320,15,3,2,2299,0,4598),

(20240323,1,4,1,69999,0,69999),
(20240324,2,5,2,75999,1500,150498),
(20240325,3,6,1,60999,0,60999),
(20240326,4,7,2,4999,0,9998),
(20240327,5,8,1,45999,0,45999);
