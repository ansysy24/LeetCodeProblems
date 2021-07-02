select distinct Salary as SecondHighestSalary
from Employee
order by SecondHighestSalary desc
limit 1 offset 1

select order_id, customer_id, freight, ship_country
from orders
where ship_country like 'N%'
order by freight
limit 10;

select * from employees
where region is null;

select count(*)
from customers
where region is not null;

select country, count(*)
from suppliers
group by country
order by count(*) desc;

select ship_country, sum(freight)
from orders
where ship_region is not null
group by ship_country
having sum(freight) > 2750
order by sum(freight) desc;

select country
from customers
intersect
select country
from suppliers
except
select country
from employees
order by country;









