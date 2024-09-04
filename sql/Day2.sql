create table tblEmployee(
id int,
Name nvarchar(50),
Gender nvarchar(20),
Salary int,
DepartmentId int,
)

Insert into tblEmployee (id,Name,Gender,Salary,DepartmentId)
Values (1,'Tom','Male',4000,1),
(4,'Sam','Male',4500,2),
(2,'Pam','Female',3000,3),
(3,'John','Male',3500,1),
(5,'Todd','Male',2800,2),
(6,'Ben','Male',7000,1),
(7,'Sara','Female',4800,3),
(8,'Valarie','Female',5500,1),
(9,'James','Male',6500,Null),
(10,'Russel','Male',8000,Null)

create table tblDepartment(
id int,
DepartmentName nvarchar(50),
[Location] nvarchar(500),
DepartmentHead nvarchar(50),
)

Insert into tblDepartment (id,DepartmentName,[Location],DepartmentHead)
Values (1,'IT','London','Rick'),
(2,'PayRoll','Delhi','Ron'),
(3,'HR','NewYork','Christie'),
(4,'Other Department','Sydney','Cinderella')

select * from tblEmployee
select * from tblDepartment

update tblDepartment set id=4 where DepartmentName='Other Department'

select name,Gender,Salary,DepartmentName from tblEmployee as e inner join tblDepartment as d on e.DepartmentId=d.id

select name,Gender,Salary,DepartmentName from tblEmployee as e left outer join tblDepartment as d on e.DepartmentId=d.id

select name,Gender,Salary,DepartmentName from tblEmployee as e Right outer join tblDepartment as d on e.DepartmentId=d.id

select name,Gender,Salary,DepartmentName from tblEmployee as e Full outer join tblDepartment as d on e.DepartmentId=d.id

create table Products(
	product_id int,
	product_name nvarchar(50),
	price int 
)

insert into Products (product_id,product_name,price)
values (1,'Laptop',800.00),
(2,'Smartphone',500.00),
(3,'Tablet',300.00),
(4,'Headphone',50.00),
(5,'Monitor',150.00)

select * from Products

Alter table Products
Alter column price Decimal(10,2)


create table Orders(
	order_id int,
	product_id int,
	quatity int,
	order_date date 
)

insert into Orders (order_id,product_id,quatity,order_date)
values (1,1,2,'2024-08-01'),
(2,2,1,'2024-08-02'),
(3,3,3,'2024-08-03'),
(4,1,1,'2024-08-04'),
(5,4,4,'2024-08-05'),
(6,5,2,'2024-08-06'),
(7,6,1,'2024-08-06')

select * from Products as p inner join Orders as o on p.product_id=o.product_id


select * from Products as p left join Orders as o on p.product_id=o.product_id


select * from Products as p right outer join Orders as o on p.product_id=o.product_id


select * from Products as p full outer join Orders as o on p.product_id=o.product_id

select p.product_name, o.order_date ,sum(o.quatity) as total_quantity 
from orders o join Products p on o.product_id=p.product_id
group by Grouping Sets ((p.product_name),(o.order_date))

select o.order_id, o.product_id,
(select p.product_name from Products as p where p.product_id=o.product_id) as product_name
from Orders as o;

select u.users_id ,u.user_name
from users u
where exists (select 1 from Orders o where o.user_id=u.user_id)

-- Subs cribed to amazon Retail -- Never Placed the order

Select order_id,order_date,product_id
from orders
where product_id in (select product_id from products where price>500)

select p.product_name,p.price
from products p
where p.price> All (select price from products where product_name like 'Smartphone%')

select p.product_name,p.price
from products p
where p.price> Any (select price from products where product_name like 'Laptop%')

--query to retrive users who have ordered products priced above 1000. The query uses two levels of nested subqueries.
select order_id from Products where price>1000
select user_id from users where user_id in (select user_id from orders where product_id in (select product_id from Products where price>1000))


CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255),
    department VARCHAR(255),
    manager_id INT
);

CREATE TABLE Salaries (
    salary_id INT PRIMARY KEY,
    employee_id INT,
    salary DECIMAL(10, 2),
    salary_date DATE,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);



INSERT INTO Employees (employee_id, employee_name, department, manager_id) VALUES
(1, 'John Doe', 'HR', NULL),
(2, 'Jane Smith', 'Finance', 1),
(3, 'Robert Brown', 'Finance', 1),
(4, 'Emily Davis', 'Engineering', 2),
(5, 'Michael Johnson', 'Engineering', 2);

INSERT INTO Salaries (salary_id, employee_id, salary, salary_date) VALUES
(1, 1, 5000, '2024-01-01'),
(2, 2, 6000, '2024-01-15'),
(3, 3, 5500, '2024-02-01'),
(4, 4, 7000, '2024-02-15'),
(5, 5, 7500, '2024-03-01');

-- Using an Equi Join:
--Write a query to list all employees and their salaries using an equi join between the Employees and Salaries tables.
select * from Employees as e  join Salaries as s on e.employee_id=s.employee_id

--Using a Self Join:
--Write a query to list each employee and their manager's name using a self join on the Employees table.
select * from Employees as e join Employees as m  on e.employee_id=m.manager_id

--Using GROUP BY with HAVING:
--Write a query to calculate the average salary by department. Use GROUP BY and filter out departments where the average salary is below 6000.

select department ,avg(salary) from Salaries as s inner join Employees as e on e.employee_id=s.employee_id group by department 

--Using GROUP BY with Grouping Sets:
--Write a query using grouping sets to calculate the total salary by department and the overall total salary.
select department ,sum(salary) from Salaries as s inner join Employees as e on e.employee_id=s.employee_id group by GROUPING sets ((department),())

--Querying Data by Using Subqueries:
--Write a query to list all employees whose salary is above the average salary using a subquery
select employee_name from employees where employee_id in (select employee_id from Salaries where salary>(select avg(salary) from Salaries))

--Using the EXISTS Keyword:
---Write a query to list all employees who have received a salary in 2024 using the EXISTS keyword.
select employee_name from Employees where employee_id in (select employee_id from salaries where  exists (select 1 from Salaries where salary_date>'2024-01-01'))

--Using the ANY Keyword:
--Write a query to find employees whose salary is greater than the salary of any employee in the Engineering department.
select salary from Salaries as s inner join Employees as e on s.employee_id=e.employee_id where department='Engineering'
(select employee_id from Salaries where Salary> Any (select salary from Salaries as s inner join Employees as e on s.employee_id=e.employee_id where department='Engineering'))
select employee_name from Employees where employee_id in (select employee_id from Salaries where Salary> Any (select salary from Salaries as s inner join Employees as e on s.employee_id=e.employee_id where department='Engineering')) and department != 'Engineering'

--Using the ALL Keyword:
--Write a query to find employees whose salary is greater than the salary of all employees in the Finance department.
