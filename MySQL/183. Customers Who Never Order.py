# Write your MySQL query statement below

SELECT c.name as Customers
FROM Customers c
LEFT JOIN Orders o on c.Id = o.CustomerId
WHERE o.Id IS NULL