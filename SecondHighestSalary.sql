select distinct Salary as SecondHighestSalary
from Employee
order by SecondHighestSalary desc
limit 1 offset 1