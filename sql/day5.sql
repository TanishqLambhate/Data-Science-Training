 CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15)
);
INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber)
VALUES 
(1, 'amit', 'sharma', 'amit.sharma@example.com', '9876543210'),
(2, 'priya', 'mehta', 'priya.mehta@example.com', '8765432109'),
(3, 'rohit', 'kumar', 'rohit.kumar@example.com', '7654321098'),
(4, 'neha', 'verma', 'neha.verma@example.com', '6543210987'),
(5, 'siddharth', 'singh', 'siddharth.singh@example.com', '5432109876'),
(6, 'asha', 'rao', 'asha.rao@example.com', '4321098765');

update Customers
set FirstName=LTRIM(RTRIM(LOWEr(firstName))),
LastName=LTRIM(RTRIM(LOWEr(LastName)))

select * from Customers
where FirstName like 'A%'

select * from Customers
where PhoneNumber like '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'

select * from Customers
where LastName like '_____'--underscore written 5 times

Select CustomerID,OrderID,TotalAmount,
		SUM(TotalAmount) Over (Partition By CustomerID Order by order_date) as RunningTotal
From Orders

Select customerID , TotalSales,
		Rank() over (Order by TotalSales Desc) As SalesRank
From (
		Select CustomerID,Sum(TotalAmount) As TotalSales
		From Orders1
		Group By CustomerID
)As SalesData

CREATE TABLE Employees1 (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeName VARCHAR(100),
    ManagerID INT NULL
);

INSERT INTO Employees1 (EmployeeName, ManagerID)
VALUES 
('Amit Sharma', NULL),  -- Top manager
('Priya Mehta', 1),     -- Reports to Amit
('Rohit Kumar', 1),     -- Reports to Amit
('Neha Verma', 2),      -- Reports to Priya
('Siddharth Singh', 2), -- Reports to Priya
('Asha Rao', 3);        -- Reports to Rohit

INSERT INTO Employees1 (EmployeeName, ManagerID)
VALUES 
('Vikram Gupta', 4),  -- Reports to Neha
('Rajesh Patel', 5);  -- Reports to Siddharth

with RecursiveEmployeeCTE As(
	Select EMployeeID , MAnagerID , EmployeeName
	From Employees1
	where ManagerID is Null
	Union ALL
	Select e.EmployeeID,e.ManagerID,e.EmployeeName
	From Employees1 e
	Inner Join RecursiveEmployeeCTE r on e.ManagerID=r.EmployeeID
)
Select * from RecursiveEmployeeCTE

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Category VARCHAR(50),
    Amount DECIMAL(10, 2),
    SaleDate DATE
);
 
INSERT INTO Sales (SaleID, ProductID, Category, Amount, SaleDate) 
VALUES 
(1, 101, 'Electronics', 1500.00, '2024-01-15'),
(2, 102, 'Furniture', 800.00, '2024-01-16'),
(3, 103, 'Electronics', 2000.00, '2024-01-17'),
(4, 104, 'Electronics', 1200.00, '2024-02-01'),
(5, 105, 'Furniture', 900.00, '2024-02-03');

Select Category,SUm(Amount) as TotalSales
from Sales
Group By Rollup (Category)

CREATE TABLE Orders2 (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderAmount DECIMAL(10, 2),
    OrderDate DATE
);
 
INSERT INTO Orders2 (OrderID, CustomerID, OrderAmount, OrderDate)
VALUES 
(1, 1, 500.00, '2024-01-15'),
(2, 2, 700.00, '2024-01-16'),
(3, 1, 300.00, '2024-01-17'),
(4, 3, 1200.00, '2024-02-01'),
(5, 2, 900.00, '2024-02-03');

select distinct o1.CustomerID
from Orders2 o1
where (
	select Count(*)
	from Orders2 o2
	where o2.CustomerID=o1.CustomerID
)>1

CREATE TABLE ProductSales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Amount DECIMAL(10, 2),
    SaleDate DATE
);
 
INSERT INTO ProductSales (SaleID, ProductID, Amount, SaleDate)
VALUES 
(1, 101, 1500.00, '2024-01-15'),
(2, 102, 800.00, '2024-01-16'),
(3, 103, 2000.00, '2024-01-17'),
(4, 104, 1200.00, '2024-02-01'),
(5, 105, 900.00, '2024-02-03');

create view TotalSalesByProduct
With SchemaBinding
As
Select ProductID , Sum(Amount) AS TotalSales
From dbo.ProductSales
Group By ProductID

Select * from TotalSalesByProduct