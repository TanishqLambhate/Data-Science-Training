--### **1. Filter and Aggregate on Join Results using SQL**
-- Task: Join the `Orders` and `Customers` tables to find the total order amount per customer and filter out customers who have spent less than $1,000.
Select c.CustomerID,sum(OrderAmount) as TotalOrderAmount 
From Orders2 as o inner join Customers as c on o.CustomerID=c.CustomerID 
Group By c.CustomerID 
Having sum(o.orderAmount)>=1000

--### **2. Cumulative Aggregations and Ranking in SQL Queries**
-- Task: Create a cumulative sum of the `OrderAmount` for each customer to track the running total of how much each customer has spent.
Select CustomerID , OrderAmount, 
Sum(OrderAmount) Over(Partition by CustomerID order by orderDate) as TotalOrderAmount
From Orders2

--### **3. OVER and PARTITION BY Clause in SQL Queries**
-- Task: Rank the customers based on the total amount they have spent, partitioned by city.
Select CustomerID , TotalOrderAmount, City,
Rank() over(Partition By City Order By TotalOrderAmount Desc)as Ranks
From (
	select o.CustomerID,c.city,sum(o.OrderAmount) as TotalOrderAmount
	from Orders2 as o
	Inner Join Customers as c on o.customerID=c.CustomerID
	Group By o.CustomerID ,c.city
) as Ranking

--### **4. Total Aggregation using OVER and PARTITION BY in SQL Queries**
-- Task: Calculate the total amount of all orders (overall total) and the percentage each customer's total spending contributes to the overall total.
With CustomerTotal As (
    Select CustomerID, Sum(OrderAmount) As TotalOrderAmount
    From Orders2
    Group By CustomerID
)
Select 
    ct.CustomerID, 
    ct.TotalOrderAmount,
    Sum(ct.TotalOrderAmount) Over () As OverallTotalAmount,
    (ct.TotalOrderAmount * 100.0 / Sum(ct.TotalOrderAmount) Over ()) As PercentageTotal
From
    CustomerTotal ct;

--### **5. Ranking in SQL**
-- Task: Rank all customers based on the total amount they have spent, without partitioning.
Select CustomerID , TotalOrderAmount, 
Rank() over(Order By TotalOrderAmount Desc)as Ranks
From (
	Select CustomerID,sum(OrderAmount) as TotalOrderAmount
	From Orders2
	Group By CustomerID
) as Ranking

--Here are additional tasks that build on the concepts of filtering, aggregating, ranking, and window functions in SQL:

--### **6. Task: Calculate the Average Order Amount per City**
-- Task: Write a query that joins the `Orders` and `Customers` tables, calculates the average order amount for each city, and orders the results by the average amount in descending order.
Select c.city,avg(OrderAmount) as AverageOrderAmount 
From Orders2 as o inner join Customers as c on o.CustomerID=c.CustomerID 
Group By c.city
order by avg(OrderAmount) Desc

--### **7. Task: Find Top N Customers by Total Spending**
--Task: Write a query to find the top 3 customers who have spent the most, using `ORDER BY` and `LIMIT`.
Select Top 3 c.CustomerID,sum(OrderAmount) as TotalOrderAmount 
From Orders2 as o inner join Customers as c on o.CustomerID=c.CustomerID 
Group By c.CustomerID
order by sum(OrderAmount) Desc

--### **8. Task: Calculate Yearly Order Totals**
-- Task: Write a query that groups orders by year (using `OrderDate`), calculates the total amount of orders for each year, and orders the results by year.
Select Year(OrderDate) as OrderYear,Sum(OrderAmount) as Total 
From orders2 
Group by year(OrderDate) 
Order by OrderYear

--### **9. Task: Calculate the Rank of Customers by Total Order Amount**
-- Task: Write a query that ranks customers by their total spending, but only for customers located in "Mumbai". The rank should reset for each customer in "Mumbai".
Select c.CustomerID,c.city,sum(o.OrderAmount) as TotalSpent ,
Rank() over(order By sum(O.OrderAmount) Desc) as Ranking
From Orders2 as o inner Join Customers as c on c.CustomerID=o.CustomerID
where c.city='Mumbai'
Group By c.CustomerID,c.City
Order By Ranking

--### **10. Task: Compare Each Customer's Total Order to the Average Order Amount**
-- Task: Write a query that calculates each customer's total order amount and compares it to the average order amount for all customers.
Select c.CustomerID,Sum(o.orderAmount) as TotalOrderAmount,
(Select Avg(orderAmount) from Orders2) as AverageOrderAmount,
Sum(o.OrderAmount)-(Select Avg(orderAmount) from Orders2) as DifferenceedAmount
From Orders2 as o 
Inner Join Customers as c on c.customerID=o.CustomerID
Group BY c.CustomerID
Order By TotalOrderAmount Desc

