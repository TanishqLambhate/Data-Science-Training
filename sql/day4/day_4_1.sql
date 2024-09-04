select product_name,price,ROUND(price,3) as roundedprice from Products

select product_name,price,floor(price) as flooredprice from Products

select product_name,price,ceiling(price) as ceilingprice from Products

select product_name,price,sqrt(price) as sqrootedprice from Products

select product_name,price,power(price,3) as poweredprice from Products

select abs(max(price)-min(price)) as poweredprice from Products

select product_name,price%5 as poweredprice from Products

select product_name,price,round(rand()*100,2) as poweredprice from Products

select product_name,price,log(price) as lograthmicprice from Products

--Scenario: Apply a 15% discount, round the discounted price to 2 decimal places, and show both the ceiling and floor values of the final discounted price.
 
 select round(0.85*price,2) ,ceiling(0.85*price),floor(0.85*price) from Products

