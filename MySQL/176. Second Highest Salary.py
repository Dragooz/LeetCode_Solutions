# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT 
        Salary 
    from 
        Employee 
    ORDER BY Salary desc LIMIT 1 OFFSET 1)
    AS SecondHighestSalary