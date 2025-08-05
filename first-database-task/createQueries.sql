CREATE TABLE Customers(
customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
customer_name VARCHAR(150),
phone_number VARCHAR(50),
email VARCHAR(50)
)

CREATE TABLE Orders(
order_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
customer_id INT,
order_number INT,
total_cost REAL,
FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
)

CREATE TABLE Products(
product_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
product_name VARCHAR(100),
barcode INT,
quantity REAL,
price REAL
)

CREATE TABLE Order_Products(
order_id INT,
product_id INT,
barcode INT,
price REAL,
PRIMARY KEY(order_id, product_id),
FOREIGN KEY(order_id) REFERENCES Orders(order_id),
FOREIGN KEY(product_id) REFERENCES Products(product_id)
)