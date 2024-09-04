![alt text](<Screenshot 2024-08-21 110850.png>) ![alt text](<Screenshot 2024-08-21 111917.png>) ![alt text](<Screenshot 2024-08-21 111021.png>) ![alt text](<Screenshot 2024-08-21 110621.png>) ![alt text](<Screenshot 2024-08-21 105643.png>) ![alt text](<Screenshot 2024-08-21 103452.png>)

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    ProductID INT NOT NULL,
    OrderDate DATE NOT NULL,
    Quantity INT NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


INSERT INTO Products (ProductID, ProductName, Category, Price, StockQuantity)
VALUES
(1, 'Laptop', 'Electronics', 75000.00, 10),
(2, 'Smartphone', 'Electronics', 25000.00, 25),
(3, 'Headphones', 'Accessories', 2000.00, 50),
(4, 'Desk Chair', 'Furniture', 5000.00, 15),
(5, 'Monitor', 'Electronics', 12000.00, 8);


INSERT INTO Orders (OrderID, ProductID, OrderDate, Quantity, TotalAmount)
VALUES
(1, 1, '2024-08-01', 2, 150000.00),
(2, 2, '2024-08-02', 3, 75000.00),
(3, 3, '2024-08-03', 5, 10000.00),
(4, 4, '2024-08-04', 1, 5000.00),
(5, 2, '2024-08-05', 1, 25000.00);

