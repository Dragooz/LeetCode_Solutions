# Write your MySQL query statement below

SELECT e.Name as Employee
FROM Employee e
WHERE e.ManagerId IS NOT NULL AND e.Salary > 
(SELECT e2.Salary from Employee e2 WHERE e2.Id = e.ManagerId)