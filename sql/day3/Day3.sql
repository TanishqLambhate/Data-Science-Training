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

CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incrementing unique identifier for each customer
    FirstName NVARCHAR(50) NOT NULL,           -- Customer's first name
    LastName NVARCHAR(50) NOT NULL,            -- Customer's last name
    Email NVARCHAR(100),                       -- Customer's email address
    OrderID INT,                               -- Foreign key to link to Orders table
    CreatedAt DATETIME DEFAULT GETDATE()       -- Record creation timestamp, defaults to the current date and time
);

-- Insert data into the Customers table
INSERT INTO Customers (FirstName, LastName, Email, OrderID)
VALUES 
('John', 'Doe', 'john.doe@example.com', 101),
('Jane', 'Smith', 'jane.smith@example.com', 102),
('Michael', 'Johnson', 'michael.johnson@example.com', 103),
('Emily', 'Davis', 'emily.davis@example.com', 104),
('David', 'Wilson', 'david.wilson@example.com', 105);



