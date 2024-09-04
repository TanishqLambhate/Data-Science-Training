create database collage

create table tblGender
(ID int Not Null Primary Key,
Gender nvarchar(50))

Alter table tblPerson
add constraint tblPerson_GenderId Foreign Key
(GenderId) references tblGender(ID)

Insert into tblGender(Id,Gender)
Values (1,'Male'),
(2,'Female'),
(3,'Others')

Insert Into tblPerson (Id,Name,Email,GenderId)
Values(1,'Tom','Tom@gmail.com',1),
(2,'Jessy','Jessy@gmail.com',2),
(3,'Kristy','Kristy@gmail.com',2),
(4,'John','John@gmail.com',1),
(5,'Rob','Rob@gmail.com',1)

Update tblPerson
set email='TomUpdated@gmail.com'
where Id=1;

Update tblPerson
set GenderId=1
where Name='Jessy';

Delete from tblPerson
where Id=3

create table Employees(
EmployeeID int not null,
FirstName nvarchar(50),
LastName nvarchar(50),
Position nvarchar(50),
Department nvarchar(50),
HireDate date
)

Insert Into Employees(EmployeeID,FirstName,LastName,Position,Department,HireDate)
Values(1,'Tom','Hardings','SDE','IT','2022-04-01'),
(2,'John','Snow','Testing','IT','2023-04-01'),
(3,'Ned','Stark','BDE','Business','2024-04-01'),
(4,'Jamie','Lannister','SDE','IT','2020-04-01'),
(5,'Robert','Baretheon','SDE','IT','2021-04-01')

Insert Into Employees(EmployeeID,FirstName,LastName,Position,Department,HireDate)
Values(3,'Ned','Stark','BDE','Business','2024-04-01')

Update Employees
set Position='Automated Tester'
where EmployeeID=1;

Delete from Employees


select Department,count(Department) as counts from Employees group by Department

select * from Employees where Department in (select Department as counts from Employees group by Department having count(*)>2)

INSERT INTO Employees (EmployeeID, FirstName, LastName, Position, Department, HireDate)
VALUES 
(1, 'Amit', 'Sharma', 'Software Engineer', 'IT', '2022-01-15'),
(2, 'Priya', 'Mehta', 'Project Manager', 'Operations', '2023-02-20'),
(3, 'Raj', 'Patel', 'Business Analyst', 'Finance', '2021-06-30'),
(4, 'Sunita', 'Verma', 'HR Specialist', 'HR', '2019-08-12'),
(5, 'Vikram', 'Rao', 'Software Engineer', 'IT', '2021-03-18'),
(6, 'Anjali', 'Nair', 'HR Manager', 'HR', '2020-05-14'),
(7, 'Rohan', 'Desai', 'Finance Manager', 'Finance', '2022-11-25'),
(8, 'Sneha', 'Kumar', 'Operations Coordinator', 'Operations', '2023-07-02'),
(9, 'Deepak', 'Singh', 'Data Scientist', 'IT', '2022-08-05'),
(10, 'Neha', 'Gupta', 'Business Analyst', 'Finance', '2020-10-10');

select * from Employees where Department='IT'

select * from Employees where HireDate>'2022-01-01'

select * from Employees where Department='Finance' or Department='HR'

select * from Employees where HireDate>'2021-01-01' and Position='Software Engineer'

SELECT * FROM EmployeeTable
WHERE LastName LIKE 'S%';

--6
SELECT * FROM EmployeeTable
WHERE FirstName LIKE '%n%';

--7
SELECT COUNT(*) AS NoOfEmployees
FROM EmployeeTable;

--8
SELECT MIN(HireDate) AS EarliestHireDate 
FROM EmployeeTable;