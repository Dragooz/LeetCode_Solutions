# Write your MySQL query statement below

SELECT d.Name as Department, e.Name as Employee, e.Salary
FROM Employee e
INNER JOIN Department d on e.DepartmentId = d.Id 
WHERE (d.Name, e.Salary) IN (

SELECT d.Name as Department, max(e.Salary)
FROM Employee e
INNER JOIN Department d on e.DepartmentId = d.Id
GROUP BY d.Name
)





