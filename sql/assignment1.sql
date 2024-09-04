select * from Orders where order_date>(select dateadd(day,-30,GETDATE()))

--Write a query to extract the year, month, and day from the current date.
select year(getdate())
select month(getdate())
select day(getdate())

--Calculate the difference in years between two given dates.
select DATEDIFF(year,'2023-01-01',GETDATE()) as DaysDifference

--Retrieve the last day of the month for a given date.
SELECT EOMONTH('2024-08-22') AS last_day_of_month;

--Convert all customer names to uppercase.
select upper(employee_name)from Employees
--Extract the first 5 characters of each product name.
select substring(product_name,1,5) from Products
--Concatenate the product name and category with a hyphen in between.
select product_name,category ,concat(product_name,'-',category) as productDetails from Products

--Replace the word 'Phone' with 'Device' in all product names.
select product_name ,replace(product_name,'Phone','Device') as updatedPName from Products

--Find the position of the letter 'a' in customer names.
select CHARINDEX('a',product_name) from Products

--Calculate the total sales amount for all orders.
select sum(price) from Orders as o join products as p on o.product_id=p.product_id
--Find the average price of products in each category.
select category,avg(price) from Products group by category
--Count the number of orders placed in each month of the year.
SELECT 
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    COUNT(*) AS order_count
FROM 
    orders
WHERE 
    YEAR(order_date) = 2024  -- Replace with the desired year
GROUP BY 
    YEAR(order_date), 
    MONTH(order_date)
ORDER BY 
    order_year, 
    order_month;
--Find the maximum and minimum order quantities.
select max(quatity),min(quatity) from Orders
--Calculate the sum of stock quantities grouped by product category.
select category,sum(StockQuantity) from Orders as o join products as p on o.ProductID=p.ProductID group by Category

select * from products

--Join Exercises
--Write a query to join the Customers and Orders tables to display customer names and their order details.
select * from customers as c join orders as o on c.orderId=o.orderId
--Perform an inner join between Products and Orders to retrieve product names and quantities sold.
select productname,quantity from products as c join orders as o on c.productId=o.ProductId
--Use a left join to display all products, including those that have not been ordered.
select * from products as c left join orders as o on c.productId=o.ProductId
--Write a query to join Employees with Departments and list employee names and their respective department names.
SELECT 
	e.Name,
    d.DepartmentName
FROM 
    tblEmployee e
JOIN 
    tblDepartment d ON e.DepartmentID = d.id;
--Perform a self-join on an Employees table to show pairs of employees who work in the same department.
SELECT 
    e1.name,
    e2.name,
    e1.DepartmentID
FROM 
    tblEmployee e1
JOIN 
    tblEmployee e2 ON e1.DepartmentID = e2.DepartmentID
WHERE 
    e1.id < e2.id;

--Subquery Exercises
--Write a query to find products whose price is higher than the average price of all products.
select * from Products where price> (select avg(price) from products)
--Retrieve customer names who have placed at least one order by using a subquery.
--Find the top 3 most expensive products using a subquery.
select * from Products where price in (select top 3 price from Products) order by price desc
--Write a query to list all employees whose salary is higher than the average salary of their department.
select * from tblEmployee where Salary>(select avg(Salary) from tblEmployee)
--Use a correlated subquery to find employees who earn more than the average salary of all employees in their department.
SELECT 
    e.name,
    e.Salary,
    e.DepartmentID
FROM 
    tblEmployee e
WHERE 
    e.Salary > (
        SELECT 
            AVG(e2.Salary)
        FROM 
            tblEmployee e2
        WHERE 
            e2.DepartmentID = e.DepartmentID
    );


