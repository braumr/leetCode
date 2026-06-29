/* Write your T-SQL query statement below */
Select e.name as Employee
From Employee e join Employee m
on e.managerid=m.id
where e.salary > m.salary