select product_name from Products
where product_id in (
	select product_id from Orders
	group by product_id
	having Count(order_id)>1
)

--product that are ordered atleast once

select product_name from Products p
where exists(select 1 from orders o where o.product_id=p.product_id)

select product_name from products
where price> All(
	select price from products
	where Category='Accessories'
	)

select product_name , upper(Product_name) as uppercaseproductname from Products

select product_name ,lower(product_name) as PNameLowerCase from Products

select product_name ,substring(product_name,1,3) as ShortName from Products

select product_name ,len(product_name) as lengths from Products

select product_name ,replace(product_name,'Phone','Device') as updatedPName from Products

select product_name ,ltrim(rtrim(product_name) )as reversedName from Products

select product_name ,charindex('e',product_name) as PositionOfE from Products

select product_name,category ,concat(product_name,'-',category) as productDetails from Products

select product_name ,left(product_name,5) as ShortName from Products

select product_name ,right(product_name,3) as LastCharacters from Products

select product_name ,reverse(product_name) as reversedName from Products
-- it increases the decimal zereos
select product_name ,format(price, 'N3') as Formattedprice from Products

select product_name ,replicate(product_name,3) as RepeatedProduct from Products

select getdate() as CurrentDate,
DATEADD(Day,10,GetDate()) as FutureDate

select DATEADD(Year,-1,GETDATE()) as DateMinus1Year

select DATEDIFF(Day,'2024-01-01',GETDATE()) as DaysDifference

select Format(GETDATE(),'MMMM dd,yyyy') as FormattedDate

--Find the no. of month since your birthday
select DATEDIFF(Month,'2024-08-15',GETDATE()) as DaysDifference

select FORMAT(getdate(),'dd-mm-yyyy') as formatteddate

select year(getdate()) as Currentyear

select month(getdate()) as monthextracted

select day(getdate()) as dayextracted
